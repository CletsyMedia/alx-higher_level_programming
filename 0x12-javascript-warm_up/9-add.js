#!/usr/bin/node

const addNum = (num1, num2) => parseInt(num1) + parseInt(num2);

const a = process.argv[2];
const b = process.argv[3];

console.log(addNum(a, b));