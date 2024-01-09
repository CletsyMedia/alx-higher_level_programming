#!/usr/bin/node

const Rectangle = require('./5-rectangle');

class Square extends Rectangle {
  constructor (size) {
    // Call the constructor of the parent class (Rectangle)
    super(size, size);
  }
}
