-- Script to create the table force_name
/* Using the specified database */
USE hbtn_0d_2;
/* Creating the table if not exists */
CREATE TABLE IF NOT EXISTS force_name (
    id INT,
    name VARCHAR(256) NOT NULL
);
