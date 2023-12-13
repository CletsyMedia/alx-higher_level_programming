-- Script to list all cities with associated states using JOIN
/* Selecting cities with associated states using LEFT JOIN */
SELECT cities.id, cities.name, states.name FROM cities LEFT JOIN states ON states.id = cities.state_id ORDER BY cities.id;
