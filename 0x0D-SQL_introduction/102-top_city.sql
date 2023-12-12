-- Select the city and average temperature for the top 3 cities during July and August
SELECT city, AVG(value) AS avg_temp
FROM temperatures
WHERE month IN (7, 8)
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3; 
