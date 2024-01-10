#!/usr/bin/node
exports.esrever = function (list) {
  const reserved = [];

  for (let i = list.length - 1; i >= 0; i--) {
    reserved.push(list[i]);
  }
  return reserved;
};
