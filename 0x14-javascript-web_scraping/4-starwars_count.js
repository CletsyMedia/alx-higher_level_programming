#!/usr/bin/node

const request = require('request');

function countMoviesWithCharacter (apiUrl, characterID, callback) {
  request(apiUrl, function (error, response, body) {
    if (error) {
      return callback(error);
    }

    if (response.statusCode !== 200) {
      return callback(new Error('Invalid response: ' + response.statusCode));
    }

    const films = JSON.parse(body).results;
    const moviesWithCharacter = films.filter(film =>
      film.characters.includes(`https://swapi-api.alx-tools.com/api/people/${characterID}/`)
    );

    callback(null, moviesWithCharacter.length);
  });
}

const apiUrl = process.argv[2];
const characterID = '18';

countMoviesWithCharacter(apiUrl, characterID, function (error, count) {
  if (error) {
    console.error('Error:', error);
    process.exit(1);
  }

  console.log(count);
});
