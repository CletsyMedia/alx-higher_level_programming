#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];

request(apiUrl, function (error, response, body) {
  if (error) {
    console.error('Error:', error);
    return;
  }

  const films = JSON.parse(body).results;
  const wedgeAntillesID = '18';

  const moviesWithWedge = films.filter(film =>
    film.characters.includes(`https://swapi-api.alx-tools.com/api/people/${wedgeAntillesID}/`)
  );

  console.log(moviesWithWedge.length);
});
