#!/usr/bin/node
const star_war = require('request');
star_war(process.argv[2], function (error, response, body) {
  if (!error) {
    const n_movies = JSON.parse(body).results;
    console.log(n_movies.reduce((count, movie) => {
      return movie.characters.find((character) => character.endsWith('/18/'))
        ? count + 1
        : count;
    }, 0));
  }
});
