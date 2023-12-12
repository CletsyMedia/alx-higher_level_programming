-- Select the state and maximum temperature for each state
SELECT state, MAX(value) AS max_temp
FROM temperatures
GROUP BY state -- Group the results by state
ORDER BY state; -- Order the result set by state name
