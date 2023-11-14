#!/usr/bin/node

const { argv } = require('process');
function factorial (a) {
  const n = Number(a);
  if (n === 0 || isNaN(n)) {
    return 1;
  }

  return n * factorial(Number(a) - 1);
}

console.log(factorial(argv[2]));
