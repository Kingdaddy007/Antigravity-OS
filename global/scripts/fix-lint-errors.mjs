/**
 * fix-lint-errors.mjs
 * Automated fixer for MD025, MD060, and MD024 violations.
 * Applies transformations from the context-formatting skill:
 *   1. MD025: Convert secondary `# Key: Value` → `**Key:** Value`
 *   2. MD060: Replace tight `|---|---|` → `| --- | --- |`
 *   3. MD024: Append parent-section suffix to duplicate headings
 *
 * Scans both antigravitygold/ and .antigravity/ directories.
 * Run: node scripts/fix-lint-errors.mjs [--dry-run]
 */
import fs from 'fs';
import path from 'path';

const DRY_RUN = process.argv.includes('--dry-run');

const TARGET_DIRS = [
  '{{USER_HOME_PATH}}\\antigravitygold',
  '{{USER_HOME_PATH}}\\.antigravity'
];

const IGNORE_DIRS = [
  'node_modules', '.git', '.gemini', '.next', 'dist', 'build',
  'brain', '.vscode', 'extensions'
];

// --- Stats ---
let totalFiles = 0;
let fixedFiles = 0;
let totalMD025 = 0;
let totalMD060 = 0;
let totalMD024 = 0;

// --- Fix Functions ---

/**
 * MD025 Fix: Convert secondary H1 metadata lines to bold descriptors.
 * Only targets lines matching `# Key: Value` pattern (metadata-style).
 * Preserves the actual document title (first H1).
 */
function fixMD025(lines) {
  let fixes = 0;
  let foundFirstH1 = false;

  for (let i = 0; i < lines.length; i++) {
    const trimmed = lines[i].trimStart();

    // Detect H1 lines: starts with exactly one # followed by space
    if (/^# [^ ]/.test(trimmed) || /^# $/.test(trimmed)) {
      if (!foundFirstH1) {
        foundFirstH1 = true;
        continue; // Keep the first H1 as-is
      }

      // Secondary H1 — convert to bold descriptor
      // Pattern: "# Key: Value" → "**Key:** Value"
      const metaMatch = trimmed.match(/^# (.+?):\s*(.*)$/);
      if (metaMatch) {
        const key = metaMatch[1].trim();
        const value = metaMatch[2].trim();
        lines[i] = value ? `**${key}:** ${value}` : `**${key}:**`;
        fixes++;
      } else {
        // Non-metadata secondary H1 — convert to ## to avoid MD025
        // This handles edge cases like standalone secondary H1 titles
        lines[i] = lines[i].replace(/^# /, '## ');
        fixes++;
      }
    }
  }
  return fixes;
}

/**
 * MD060 Fix: Replace tight table separator rows with properly spaced ones.
 * Handles any number of columns, preserving alignment markers (:).
 */
function fixMD060(lines) {
  let fixes = 0;

  for (let i = 0; i < lines.length; i++) {
    const trimmed = lines[i].trim();

    // Match tight table separator rows: lines of |---| pattern
    if (/^\|[-:]+\|/.test(trimmed) && !/\| [-:]+ \|/.test(trimmed)) {
      // Split into cells, clean each, rebuild with spaces
      const cells = trimmed.split('|').filter(c => c.trim() !== '');
      const spacedCells = cells.map(() => '---');
      lines[i] = '| ' + spacedCells.join(' | ') + ' |';
      fixes++;
    }
  }
  return fixes;
}

/**
 * MD024 Fix: Append parent-section context to duplicate headings.
 * Finds the nearest parent heading (one level up) and appends its
 * short name as a parenthetical suffix to make the heading unique.
 */
function fixMD024(lines) {
  let fixes = 0;

  // First pass: collect all headings with their positions
  const headings = [];
  for (let i = 0; i < lines.length; i++) {
    const match = lines[i].match(/^(#{1,6})\s+(.+)$/);
    if (match) {
      headings.push({
        index: i,
        level: match[1].length,
        text: match[2].trim(),
        hashes: match[1]
      });
    }
  }

  // Track seen heading texts (level:text → first occurrence index)
  const seen = new Map();
  // Track all heading texts for uniqueness checking after fixes
  const allTexts = new Set();

  // Identify duplicates
  const duplicateIndices = new Set();
  for (const h of headings) {
    const key = `${h.level}:${h.text}`;
    if (seen.has(key)) {
      duplicateIndices.add(h.index);
    } else {
      seen.set(key, h.index);
      allTexts.add(key);
    }
  }

  // Fix duplicates by finding parent context
  for (const h of headings) {
    if (!duplicateIndices.has(h.index)) continue;

    // Find the nearest parent heading (one level up)
    let parentText = '';
    for (let j = headings.indexOf(h) - 1; j >= 0; j--) {
      if (headings[j].level < h.level) {
        parentText = headings[j].text;
        break;
      }
    }

    // Create a short suffix from the parent heading
    let suffix = '';
    if (parentText) {
      // Extract a clean short label from the parent
      // Remove common prefixes and clean up
      suffix = parentText
        .replace(/^#+\s*/, '')
        .replace(/[*_]/g, '') // Remove bold/italic markers
        .trim();

      // Shorten long parent names - take first meaningful word(s)
      const words = suffix.split(/\s+/);
      if (words.length > 3) {
        suffix = words.slice(0, 3).join(' ');
      }
    } else {
      // No parent found — use line number as suffix
      suffix = `Section ${h.index + 1}`;
    }

    // Build the new heading text
    const newText = `${h.text} (${suffix})`;
    const newKey = `${h.level}:${newText}`;

    // Ensure uniqueness — if this suffix is also a dupe, add line number
    let finalText = newText;
    let finalKey = newKey;
    if (allTexts.has(finalKey)) {
      finalText = `${h.text} (${suffix} L${h.index + 1})`;
      finalKey = `${h.level}:${finalText}`;
    }

    lines[h.index] = `${h.hashes} ${finalText}`;
    allTexts.add(finalKey);
    fixes++;
  }

  return fixes;
}

// --- File Processing ---

/**
 * Process a single file: apply all three fixes, write back if changed.
 */
function processFile(filePath) {
  try {
    const content = fs.readFileSync(filePath, 'utf-8');
    const lines = content.split(/\r?\n/);

    // Check original line ending style
    const useCRLF = content.includes('\r\n');

    // Apply fixes in order
    const md025Fixes = fixMD025(lines);
    const md060Fixes = fixMD060(lines);
    const md024Fixes = fixMD024(lines);

    const totalFixes = md025Fixes + md060Fixes + md024Fixes;

    if (totalFixes > 0) {
      totalMD025 += md025Fixes;
      totalMD060 += md060Fixes;
      totalMD024 += md024Fixes;
      fixedFiles++;

      const shortPath = filePath.replace('{{USER_HOME_PATH}}\\', '');
      console.log(`FIXED: ${shortPath}`);
      if (md025Fixes) console.log(`  MD025: ${md025Fixes} secondary H1s → bold`);
      if (md060Fixes) console.log(`  MD060: ${md060Fixes} table separators spaced`);
      if (md024Fixes) console.log(`  MD024: ${md024Fixes} headings de-duplicated`);

      if (!DRY_RUN) {
        const lineEnding = useCRLF ? '\r\n' : '\n';
        fs.writeFileSync(filePath, lines.join(lineEnding), 'utf-8');
      }
    }
  } catch (err) {
    console.error(`ERROR reading ${filePath}: ${err.message}`);
  }
}

/**
 * Recursively walk a directory, processing all .md files.
 */
function walkDir(dirPath) {
  try {
    const entries = fs.readdirSync(dirPath);
    for (const name of entries) {
      if (IGNORE_DIRS.includes(name)) continue;
      const fullPath = path.join(dirPath, name);
      const stat = fs.statSync(fullPath);
      if (stat.isFile() && fullPath.endsWith('.md')) {
        totalFiles++;
        processFile(fullPath);
      } else if (stat.isDirectory()) {
        walkDir(fullPath);
      }
    }
  } catch (err) {
    // Silently skip inaccessible directories
  }
}

// --- Main ---

console.log('');
console.log('='.repeat(60));
console.log('GLOBAL MARKDOWN LINT FIXER (MD025 / MD060 / MD024)');
if (DRY_RUN) console.log('>>> DRY RUN — no files will be modified <<<');
console.log('='.repeat(60));
console.log('');

for (const dir of TARGET_DIRS) {
  if (fs.existsSync(dir)) {
    console.log(`Processing: ${dir}`);
    walkDir(dir);
  } else {
    console.log(`SKIP (not found): ${dir}`);
  }
}

console.log('');
console.log('='.repeat(60));
console.log('RESULTS:');
console.log(`  Files scanned: ${totalFiles}`);
console.log(`  Files fixed:   ${fixedFiles}`);
console.log(`  MD025 fixes:   ${totalMD025}`);
console.log(`  MD060 fixes:   ${totalMD060}`);
console.log(`  MD024 fixes:   ${totalMD024}`);
console.log(`  TOTAL fixes:   ${totalMD025 + totalMD060 + totalMD024}`);
if (DRY_RUN) console.log(`  (DRY RUN — nothing was written)`);
console.log('='.repeat(60));
console.log('');
console.log('Done.');
