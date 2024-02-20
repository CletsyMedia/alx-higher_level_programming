#!/usr/bin/node

const fs = require('fs');
const request = require('request');

request(process.argv[2]).pipe(fs.createWriteStream(process.argv[3])).on('finish', () => {
  console.log(`The content has been saved to ${process.argv[3]}`);
});
