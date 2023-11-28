#!/usr/bin/node
const starwar = require('request');

starwar(process.argv[2], function (error, response, body) {
  if (!error) {
    const nmovies = JSON.parse(body).results;
    console.log(nmovies.reduce((count, movie) => {
      return movie.characters.find((character) => character.endsWith('/18/'))
        ? count + 1
        : count;
    }, 0));
  }
});
