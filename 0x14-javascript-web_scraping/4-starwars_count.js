#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];
const characterID = '18';

request(apiUrl, (error, response, body) => {
  if (error || response.statusCode !== 200) {
    console.error('Error:', error || 'Invalid response:', response.statusCode);
    process.exit(1);
  }

  const count = JSON.parse(body).results.filter(film =>
    film.characters.includes(`https://swapi-api.alx-tools.com/api/people/${characterID}/`)
  ).length;

  console.log(count);
});
