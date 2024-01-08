#!/usr/bin/node

const numSize = parseInt(process.argv[2]);

if (!isNaN(numSize) || numSize <= 0) {
  console.log('Missing size');
} else {
  for (let a = 0; a < numSize; a++) {
    let row = '';
    for (let b = 0; b < numSize; b++) {
      row += 'X';
    }
    console.log(row);
  }
}
