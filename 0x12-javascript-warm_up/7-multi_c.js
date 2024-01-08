#!/usr/bin/node

const args = process.argv.slice(2);

if (isNaN(args[0])) {
  console.log('Missing number of occurrences');
} else {
  const times = parseInt(args[0]);
  for (let i = 0; i < times; i++) {
    console.log('C is fun');
  }
}
