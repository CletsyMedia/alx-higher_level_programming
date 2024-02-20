#!/usr/bin/node

const request = require('request');

// Check if the correct number of command-line arguments are provided
if (process.argv.length !== 3) {
  console.error('Usage: ./2-statuscode.js <URL>');
  process.exit(1);
}

const url = process.argv[2];

// Make a GET request to the provided URL
request.get(url, function (error, response) {
  if (error) {
    console.error(error);
    process.exit(1);
  }
  console.log('code:', response.statusCode);
});
