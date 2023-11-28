#!/usr/bin/node
const filepath = require('fs');

filepath.writeFile(process.argv[2], process.argv[3], error => {
  if (error) console.log(error);
});
