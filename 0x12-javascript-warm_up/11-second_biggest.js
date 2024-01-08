#!/usr/bin/node

function secBig(arr) {
  if (arr.length <= 1) {
    return 0;
  }

  const sortedArr = arr.sort(function(a, b) {
    return b - a;
  });

  return sortedArr[1];
}

const args = process.argv.slice(2).map(Number);

if (args.length <= 1) {
  console.log(0);
} else {
  console.log(secBig(args));
}
