-- Import the table dump into the hbtn_0c_0 database
SELECT city, AVG(value) AS avg_temp
FROM temperatures
GROUP BY city
ORDER BY avg_temp DESC;
