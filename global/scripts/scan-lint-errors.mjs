/**
 * scan-lint-errors.mjs
 * Zero-quota local scanner for MD025, MD060, and MD024 violations.
 * Scans all .md files in antigravitygold/ and .antigravity/ (excluding extensions, node_modules, .git).
 * Outputs a structured report of every violation found per file.
 */
import fs from 'fs';
import path from 'path';

const TARGET_DIRS = [
  '{{USER_HOME_PATH}}\\antigravitygold',
  '{{USER_HOME_PATH}}\\.antigravity'
];

const IGNORE_DIRS = [
  'node_modules', '.git', '.gemini', '.next', 'dist', 'build',
  'brain', '.vscode', 'extensions'
];

// --- Detection Functions ---

/**
 * MD025: Multiple top-level headings (# H1).
 * Returns array of { line, content } for every H1 AFTER the first one.
 */
function detectMD025(lines) {
  const violations = [];
  let foundFirst = false;
  for (let i = 0; i < lines.length; i++) {
    const trimmed = lines[i].trimStart();
    // Match lines starting with exactly one # followed by a space (H1)
    if (/^# [^ ]/.test(trimmed) || /^# $/.test(trimmed)) {
      if (!foundFirst) {
        foundFirst = true;
      } else {
        violations.push({ line: i + 1, content: lines[i].trim() });
      }
    }
  }
  return violations;
}

/**
 * MD060: Table separator rows with compact/tight pipes (no spaces).
 * Matches lines like |---|---| or |:---|:---| that lack spaces around pipes.
 */
function detectMD060(lines) {
  const violations = [];
  for (let i = 0; i < lines.length; i++) {
    const trimmed = lines[i].trim();
    // Only check table separator rows
    if (/^\|[-:]+\|/.test(trimmed)) {
      // Check if ANY internal pipe lacks surrounding spaces
      // A properly spaced separator looks like: | --- | --- |
      // A tight separator looks like: |---|---| or |:---|:---|
      if (/\|[-:]+\|/.test(trimmed) && !/\| [-:]+ \|/.test(trimmed)) {
        violations.push({ line: i + 1, content: lines[i].trim() });
      }
    }
  }
  return violations;
}

/**
 * MD024: Duplicate heading content.
 * Returns array of { line, content } for every heading whose text duplicates
 * an earlier heading at the same level.
 */
function detectMD024(lines) {
  const violations = [];
  const seen = new Map(); // key = "level:text", value = first line number
  for (let i = 0; i < lines.length; i++) {
    const match = lines[i].match(/^(#{1,6})\s+(.+)$/);
    if (match) {
      const level = match[1].length;
      const text = match[2].trim();
      const key = `${level}:${text}`;
      if (seen.has(key)) {
        violations.push({ line: i + 1, content: lines[i].trim(), firstSeen: seen.get(key) });
      } else {
        seen.set(key, i + 1);
      }
    }
  }
  return violations;
}

// --- File Processing ---

function scanFile(filePath) {
  try {
    const content = fs.readFileSync(filePath, 'utf-8');
    const lines = content.split(/\r?\n/);

    const md025 = detectMD025(lines);
    const md060 = detectMD060(lines);
    const md024 = detectMD024(lines);

    if (md025.length + md060.length + md024.length > 0) {
      return { filePath, md025, md060, md024 };
    }
  } catch (err) {
    // Silently skip unreadable files
  }
  return null;
}

function walkDir(dirPath, results) {
  try {
    const entries = fs.readdirSync(dirPath);
    for (const name of entries) {
      if (IGNORE_DIRS.includes(name)) continue;
      const fullPath = path.join(dirPath, name);
      const stat = fs.statSync(fullPath);
      if (stat.isFile() && fullPath.endsWith('.md')) {
        const result = scanFile(fullPath);
        if (result) results.push(result);
      } else if (stat.isDirectory()) {
        walkDir(fullPath, results);
      }
    }
  } catch (err) {
    // Silently skip inaccessible directories
  }
}

// --- Main ---

console.log('');
console.log('='.repeat(60));
console.log('GLOBAL MARKDOWN LINT SCANNER (MD025 / MD060 / MD024)');
console.log('='.repeat(60));
console.log('');

const allResults = [];

for (const dir of TARGET_DIRS) {
  if (fs.existsSync(dir)) {
    console.log(`Scanning: ${dir}`);
    walkDir(dir, allResults);
  } else {
    console.log(`SKIP (not found): ${dir}`);
  }
}

console.log('');

if (allResults.length === 0) {
  console.log('All files are clean!');
} else {
  // Summary table
  let totalMD025 = 0, totalMD060 = 0, totalMD024 = 0;

  for (const r of allResults) {
    totalMD025 += r.md025.length;
    totalMD060 += r.md060.length;
    totalMD024 += r.md024.length;

    // Shorten path for readability
    const short = r.filePath.replace('{{USER_HOME_PATH}}\\', '');
    console.log(`FILE: ${short}`);

    if (r.md025.length > 0) {
      console.log(`  MD025 (${r.md025.length} extra H1s):`);
      for (const v of r.md025) {
        console.log(`    Line ${v.line}: ${v.content.substring(0, 60)}`);
      }
    }
    if (r.md060.length > 0) {
      console.log(`  MD060 (${r.md060.length} tight table separators):`);
      for (const v of r.md060) {
        console.log(`    Line ${v.line}: ${v.content.substring(0, 80)}`);
      }
    }
    if (r.md024.length > 0) {
      console.log(`  MD024 (${r.md024.length} duplicate headings):`);
      for (const v of r.md024) {
        console.log(`    Line ${v.line}: ${v.content.substring(0, 60)} (first at line ${v.firstSeen})`);
      }
    }
    console.log('');
  }

  console.log('='.repeat(60));
  console.log('TOTALS:');
  console.log(`  Files affected: ${allResults.length}`);
  console.log(`  MD025 violations: ${totalMD025}`);
  console.log(`  MD060 violations: ${totalMD060}`);
  console.log(`  MD024 violations: ${totalMD024}`);
  console.log(`  TOTAL violations: ${totalMD025 + totalMD060 + totalMD024}`);
  console.log('='.repeat(60));
}

console.log('');
console.log('Scan complete.');
