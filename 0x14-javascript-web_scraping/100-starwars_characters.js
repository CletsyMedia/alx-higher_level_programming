#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];

const apiUrl = `https://swapi.dev/api/films/${movieId}/`;

request(apiUrl, function (error, response, body) {
  if (error) {
    console.error('Error:', error);
  } else {
    const film = JSON.parse(body);
    const charactersUrls = film.characters;

    charactersUrls.forEach(characterUrl => {
      request(characterUrl, function (error, response, body) {
        if (error) {
          console.error('Error:', error);
        } else {
          const character = JSON.parse(body);
          console.log(character.name);
        }
      });
    });
  }
});
