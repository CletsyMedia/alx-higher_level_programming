-- Import the table dump into the hbtn_0c_0 database
SELECT city, AVG(temperature) AS avg_temp
FROM your_imported_table_name
GROUP BY city
ORDER BY avg_temp DESC;
