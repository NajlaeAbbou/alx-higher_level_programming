#!/usr/bin/node
const fs = require('fs');
const request = require('request');
fs(process.argv[2]).pipe(fs.createWriteStream(process.argv[3]));
