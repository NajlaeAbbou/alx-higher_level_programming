#!/usr/bin/node
const star_war = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];
star_war(url, function (error, response, body) {
  console.log(error || JSON.parse(body).title);
});
