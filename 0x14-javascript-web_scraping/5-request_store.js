#!/usr/bin/node
const file_path = require('fs');
const result = require('request');
file_path(process.argv[2]).pipe(file_path.createWriteStream(process.argv[3]));
