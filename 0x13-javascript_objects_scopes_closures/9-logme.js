#!/usr/bin/node

let counter = 0;

exports.logMe = (item) => {
  console.log(`${counter}: ${item}`);
  counter++;
};
