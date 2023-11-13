#!/usr/bin/node

const { argv } = require('process');

if (argv.length === 2) {
  console.log('Missing number of occurrences');
} else {
  const number = Number(argv[2]);
  for (let i = 0; i < number; i++) {
    console.log('C is fun');
  }
}
