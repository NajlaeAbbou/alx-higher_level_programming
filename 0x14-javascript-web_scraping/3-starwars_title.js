#!/usr/bin/node
const starwar = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

starwar(url, function (error, response, body) {
  console.log(error || JSON.parse(body).title);
});
