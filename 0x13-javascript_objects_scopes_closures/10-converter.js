#!/usr/bin/node

exports.converter = (base) => {
  return function (number) {
    return number.toString(base);
  };
};
