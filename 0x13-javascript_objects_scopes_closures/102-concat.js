#!/usr/bin/node
const fs = require('fs');

const fileACont = fs.readFileSync(process.argv[2]).toString();
const fileBCont = fs.readFileSync(process.argv[3]).toString();
fs.writeFileSync(process.argv[4], fileACont + fileBCont);
