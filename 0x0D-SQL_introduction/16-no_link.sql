-- Listing all records with a score and a name, excluding rows without a name value
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
