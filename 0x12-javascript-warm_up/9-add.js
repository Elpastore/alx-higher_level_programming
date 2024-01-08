#!/usr/bin/node

function add (a, b) {
  return (a + b);
}
const ars = process.argv.slice(2);

console.log(add(parseInt(ars[0]), parseInt(ars[1])));
