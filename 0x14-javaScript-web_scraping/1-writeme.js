#!/usr/bin/node

const fs = require('fs');

// Check if the correct number of command-line arguments are provided
if (process.argv.length !== 4) {
  console.error('Usage: ./1-writeme.js <file_path> <string_to_write>');
  process.exit(1);
}

const filePath = process.argv[2];
const stringToWrite = process.argv[3];

// Write the string to the file asynchronously
fs.writeFile(filePath, stringToWrite, 'utf8', function (error) {
  if (error) {
    console.error(error);
    process.exit(1);
  }
});
