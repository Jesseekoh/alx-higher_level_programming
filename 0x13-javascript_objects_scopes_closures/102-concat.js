#!/usr/bin/node

const fs = require('fs');
const { argv } = require('process');

const file1 = fs.readFileSync(argv[2], 'utf8');
const file2 = fs.readFileSync(argv[3], 'utf8');

fs.writeFileSync(argv[4], file1 + file2);
