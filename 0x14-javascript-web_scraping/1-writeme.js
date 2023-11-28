#!/usr/bin/node
const file_path = require('fs');
file_path.writeFile(process.argv[2], process.argv[3], error => {
  if (error) console.log(error);
});
