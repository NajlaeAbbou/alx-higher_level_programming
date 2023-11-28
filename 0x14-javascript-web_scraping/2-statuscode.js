#!/usr/bin/node
const status_code = require('request');
status_code.get(process.argv[2]).on('response', function (response) {
  console.log(`code: ${response.statusCode}`);
});
