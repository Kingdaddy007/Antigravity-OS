import fs from 'fs';
import path from 'path';

const TARGET_DIRS = [
  '{{USER_HOME_PATH}}\\antigravitygold',
  '{{USER_HOME_PATH}}\\.antigravity'
];

const IGNORE_DIRS = ['node_modules', '.git', '.gemini', '.next', 'dist', 'build', 'brain', '.vscode', 'extensions'];

function isLikelyBrokenTableRow(line, lineIndex, lines) {
  let text = line.trim();
  
  if (text.length === 0) return false;
  if (text.startsWith('```')) return false;
  if (text.startsWith('<!--') || text.startsWith('<')) return false;
  if (text.match(/^#+ /)) return false; // Ignore headings
  if (text.startsWith('>')) return false; // Ignore blockquotes
  
  // Ignore ASCII diagram characters (trees, lines, arrows)
  if (text.includes('├──') || text.includes('└──') || text.includes('│') || text.includes('→')) return false;

  // Case 1: Pipe-separated but missing table formatting (broken markdown table)
  // We count it if it has pipes, but we need to ensure the whole block doesn't have a |---| row
  // We'll handle this at the block level rather than line level, but for now let's just flag lines with multiple spaces.
  
  // Strip bullet points to check the content
  let contentText = text.replace(/^[-*+] /, '').replace(/^\d+\. /, '').trim();

  // Split the line by 2 or more spaces or a tab
  const segments = contentText.split(/ {2,}|\t+/);
  const validSegments = segments.filter(s => s.trim().length > 0);
  
  if (validSegments.length >= 2) {
    // Ignore simple Key: [Value] lists if they are the ONLY thing
    // Actually, Key: Value with huge spacing might be a 2-column table. Let's keep it if spacing is 3+ spaces.
    const hasLargeSpace = contentText.match(/ {3,}|\t+/);
    if (!hasLargeSpace && validSegments.length === 2 && validSegments[0].endsWith(':')) return false;
    
    return true;
  }

  return false;
}

function scanFileForBrokenTables(filePath) {
  try {
    const content = fs.readFileSync(filePath, 'utf-8');
    const lines = content.split('\n');
    let consecutiveTableRowLines = 0;
    let startLine = -1;
    let findings = [];
    let inCodeBlock = false;

    // We also want to find invalid pipe tables (no separator row)
    // Let's do a simple heuristic: a block of lines with '|' but no line matching /\|-+\|/
    let pipeBlockStart = -1;
    let pipeBlockLines = [];

    for (let i = 0; i < lines.length; i++) {
        let text = lines[i].trim();
        
        if (text.startsWith('```')) {
            inCodeBlock = !inCodeBlock;
            continue;
        }

        if (inCodeBlock) continue;

        // Check for space-separated columns
        if (isLikelyBrokenTableRow(lines[i], i, lines)) {
            if (consecutiveTableRowLines === 0) startLine = i + 1;
            consecutiveTableRowLines++;
        } else {
            // A table needs at least 2 rows to be a table
            if (consecutiveTableRowLines >= 2) {
                findings.push(`Lines ${startLine} - ${i} : Space-aligned text`);
            }
            consecutiveTableRowLines = 0;
        }

        // Check for pipe tables
        if (text.includes('|') && text.length > 3 && !text.includes('├──')) {
            if (pipeBlockStart === -1) pipeBlockStart = i + 1;
            pipeBlockLines.push(text);
        } else {
            if (pipeBlockLines.length >= 2) {
                // We have a block of pipe lines. Does it have a separator?
                const hasSeparator = pipeBlockLines.some(l => l.match(/\|[\s-:]+\|/));
                if (!hasSeparator) {
                    findings.push(`Lines ${pipeBlockStart} - ${i} : Pipe-separated but missing markdown separator (---)`);
                }
            }
            pipeBlockStart = -1;
            pipeBlockLines = [];
        }
    }
    
    if (consecutiveTableRowLines >= 2) {
        findings.push(`Lines ${startLine} - ${lines.length} : Space-aligned text`);
    }
    if (pipeBlockLines.length >= 2) {
        const hasSeparator = pipeBlockLines.some(l => l.match(/\|[\s-:]+\|/));
        if (!hasSeparator) {
            findings.push(`Lines ${pipeBlockStart} - ${lines.length} : Pipe-separated but missing markdown separator (---)`);
        }
    }

    if (findings.length > 0) {
        console.log(`\n📄 ${filePath}`);
        findings.forEach(f => console.log(`   🟡 Suspicious Table: ${f}`));
    }
  } catch (err) {
    if (err.code !== 'EISDIR') {}
  }
}

function walkDir(currentDirPath) {
  try {
    const files = fs.readdirSync(currentDirPath);
    for (const name of files) {
      if (IGNORE_DIRS.includes(name)) continue;
      const filePath = path.join(currentDirPath, name);
      const stat = fs.statSync(filePath);
      if (stat.isFile() && filePath.endsWith('.md')) {
        scanFileForBrokenTables(filePath);
      } else if (stat.isDirectory()) {
        walkDir(filePath);
      }
    }
  } catch(err) {}
}

console.log('🔍 INITIATING SMARTER TABLE SCAN...');
TARGET_DIRS.forEach(dir => {
    if (fs.existsSync(dir)) walkDir(dir);
});
console.log('\n✅ Global Scan Complete.\n');
