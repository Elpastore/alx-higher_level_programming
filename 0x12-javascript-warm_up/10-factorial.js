#!/usr/bin/node

const args = parseInt(process.argv[2]);

function factorial (number) {
  if (number === 0 || isNaN(number)) {
    return (1);
  } else {
    return (factorial(number - 1) * number);
  }
}

console.log(factorial(args));
