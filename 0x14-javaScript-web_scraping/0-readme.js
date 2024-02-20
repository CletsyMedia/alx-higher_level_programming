#!/usr/bin/node

const fs = require('fs');

// Check if a file path is provided as a command-line argument
if (process.argv.length !== 3) {
  console.error('Usage: ./read_file.js <file_path>');
  process.exit(1);
}

const filePath = process.argv[2];

// Read the content of the file asynchronously
fs.readFile(filePath, 'utf8', function (error, content) {
  if (error) {
    console.error(error);
    process.exit(1);
  }
  console.log(content);
});
