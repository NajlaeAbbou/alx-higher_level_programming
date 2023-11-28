#!/usr/bin/node
const file_path = require('fs');
file_path.readFile(process.argv[2], 'utf8', function (error, content) {
  console.log(error || content);
});
