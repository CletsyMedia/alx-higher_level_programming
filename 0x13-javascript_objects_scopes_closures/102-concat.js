#!/usr/bin/node
const fs = require('fs');

const fileAContent = fs.readFileSync(process.argv[2]).toString();
const fileBContent = fs.readFileSync(process.argv[3]).toString();
fs.writeFileSync(process.argv[4], fileAContent + fileBContent);
