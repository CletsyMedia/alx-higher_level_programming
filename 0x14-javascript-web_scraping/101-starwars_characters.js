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
    const charactersPromises = charactersUrls.map(characterUrl => {
      return new Promise((resolve, reject) => {
        request(characterUrl, function (error, response, body) {
          if (error) {
            reject(error);
          } else {
            const character = JSON.parse(body);
            resolve(character.name);
          }
        });
      });
    });
    Promise.all(charactersPromises)
      .then(characters => {
        characters.forEach(character => console.log(character));
      })
      .catch(error => {
        console.error('Error:', error);
      });
  }
});
