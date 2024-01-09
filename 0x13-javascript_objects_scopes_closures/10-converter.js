#!/usr/bin/node

exports.converter = (base) => {
  return (number) => {
    return number.toString(base);
  };
};
