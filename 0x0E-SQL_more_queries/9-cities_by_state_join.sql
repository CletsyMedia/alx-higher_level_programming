-- Script to list all cities with associated states using JOIN
/* Selecting cities with associated states using JOIN */
SELECT cities.id, cities.name, states.name AS state_name
FROM cities
LEFT JOIN states ON cities.state_id = states.id
ORDER BY cities.id ASC;
