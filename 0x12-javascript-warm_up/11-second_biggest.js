#!/usr/bin/node

function secBig(arr) {
  if (arr.length <= 1) {
    return 0;
  }

  let first = parseInt(arr[0]);
  let second = parseInt(arr[1]);

  for (let i = 2; i < arr.length; i++) {
    const currNum = parseInt(arr[i]);

    if (currNum > first) {
      second = first;
      first = currNum;
    } else if (currNum > second && currNum !== first) {
      second = currNum;
    }
  }

  return second;
}

const args = process.argv.slice(2);
console.log(secBig(args));
