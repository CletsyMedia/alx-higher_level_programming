#!/usr/bin/node

const request = require('request');
const fs = require('fs');

const url = process.argv[2];
const filePath = process.argv[3];

request(url, function (error, response, body) {
  if (error || response.statusCode !== 200) {
    console.error('Error:', error || 'Invalid response:', response.statusCode);
    process.exit(1);
  }

  fs.writeFile(filePath, body, 'utf-8', function (err) {
    if (err) {
      console.error('Error writing to file:', err);
      process.exit(1);
    }
    console.log(`The content has been saved to ${filePath}`);
  });
});
