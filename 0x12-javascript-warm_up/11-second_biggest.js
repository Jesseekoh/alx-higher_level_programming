#!/usr/bin/node

const { argv } = require('process');

if (argv.length <= 3) {
  console.log(0);
} else {
  let max = argv[2];
  for (let i = 2; i < argv.length; i++) {
    if (max < argv[i]) {
      max = argv[i];
    }
  }
  console.log(max);
}
