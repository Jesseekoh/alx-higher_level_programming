#!/usr/bin/node

const { argv } = require('process');

function add(a, b) {
	console.log(Number(argv[2]) + Number(argv[3]));
}

add(argv[2], argv[3]);
