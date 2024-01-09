#!/usr/bin/node

const data = require('./100-data');

const list = data.list;
const newList = list.map(function(value, index) {
  return value * index;
});

console.log(list);
console.log(newList);
