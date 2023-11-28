#!/usr/bin/node
const filep = require('fs');
const res = require('request');

res(process.argv[2]).pipe(filep.createWriteStream(process.argv[3]));
