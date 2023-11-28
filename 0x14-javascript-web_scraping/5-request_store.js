#!/usr/bin/node
const file_p = require('fs');
const res = require('request');
res(process.argv[2]).pipe(file_p.createWriteStream(process.argv[3]));
