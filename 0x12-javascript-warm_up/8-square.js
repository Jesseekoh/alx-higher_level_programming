#!/usr/bin/node

const { argv } = require('process');

const size = Number(argv[2]);
if (!isNaN(size)) {
  for (let i = 0; i < Number(argv[2]); i++) {
    console.log('X'.repeat(Number(argv[2])));
  }
} else {
  console.log('Missing size');
}
