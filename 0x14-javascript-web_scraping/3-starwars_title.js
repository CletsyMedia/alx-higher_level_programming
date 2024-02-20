#!/usr/bin/node

const request = require('request');

// Check if the correct number of command-line arguments are provided
if (process.argv.length !== 3) {
  console.error('Usage: ./3-starwars_title.js <movie_id>');
  process.exit(1);
}

const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

// Make a GET request to the Star Wars API with the provided movie ID
request.get(apiUrl, function (error, response, body) {
  if (error) {
    console.error(error);
    process.exit(1);
  }

  // Check if the status code is successful (200)
  if (response.statusCode === 200) {
    const movieData = JSON.parse(body);
    console.log(movieData.title);
  } else {
    console.error(`Failed to retrieve movie data. Status code: ${response.statusCode}`);
    process.exit(1);
  }
});
