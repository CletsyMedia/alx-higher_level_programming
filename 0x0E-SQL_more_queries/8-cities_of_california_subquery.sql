-- 8-cities_of_california_subquery.sql
-- Script to list all cities of California without using JOIN

/* Using the specified database */
-- USE hbtn_0d_usa;
/* Selecting cities of California using a subquery */
SELECT *
FROM cities
WHERE state_id = (SELECT id FROM states WHERE name = 'California')
ORDER BY id ASC;
