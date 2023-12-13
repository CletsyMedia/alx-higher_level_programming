-- Script to list all cities with associated states using JOIN
/* Using the specified database */
USE hbtn_0d_usa;
/* Selecting cities with associated states using JOIN */
SELECT cities.id, cities.name, states.name AS state_name
FROM cities
JOIN states ON cities.state_id = states.id
ORDER BY cities.id ASC;
