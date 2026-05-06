import fs from 'fs';
import path from 'path';

const TARGET_DIRECTORIES = ['contexts', 'skills', 'core'];
const PROJECT_ROOT = '{{USER_HOME_PATH}}/antigravitygold';
const VERSION_HISTORY_HEADING = '## VERSION HISTORY';

function processDirectory(dirPath) {
  if (!fs.existsSync(dirPath)) {
    console.log(`Directory not found: ${dirPath}`);
    return;
  }

  const entries = fs.readdirSync(dirPath, { withFileTypes: true });

  for (const entry of entries) {
    const fullPath = path.join(dirPath, entry.name);
    if (entry.isDirectory()) {
      processDirectory(fullPath);
    } else if (entry.isFile() && entry.name.endsWith('.md')) {
      removeVersionHistory(fullPath);
    }
  }
}

function removeVersionHistory(filePath) {
  try {
    const content = fs.readFileSync(filePath, 'utf8');
    const lines = content.split('\n');
    let versionHistoryIndex = -1;

    for (let i = 0; i < lines.length; i++) {
        // Case-insensitive search for ## VERSION HISTORY
      if (lines[i].trim().toUpperCase() === VERSION_HISTORY_HEADING) {
        versionHistoryIndex = i;
        break;
      }
    }

    if (versionHistoryIndex !== -1) {
      console.log(`Found Version History in: ${filePath}`);
      // Remove everything from the heading to the end
      const newLines = lines.slice(0, versionHistoryIndex);
      
      // Filter out trailing blank lines
      while (newLines.length > 0 && newLines[newLines.length - 1].trim() === '') {
        newLines.pop();
      }
      
      // Write back with a single trailing newline
      const newContent = newLines.join('\n').trimEnd() + '\n';
      fs.writeFileSync(filePath, newContent, 'utf8');
      console.log(`  Successfully removed section from ${path.basename(filePath)}`);
    }
  } catch (error) {
    console.error(`Error processing ${filePath}: ${error.message}`);
  }
}

console.log('Starting Version History removal process...');
TARGET_DIRECTORIES.forEach(dir => {
  const fullDirPath = path.resolve(PROJECT_ROOT, dir);
  processDirectory(fullDirPath);
});
console.log('Process complete.');
