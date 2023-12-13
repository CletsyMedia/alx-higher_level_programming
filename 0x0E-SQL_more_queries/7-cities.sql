-- Script to create the database hbtn_0d_usa and the table cities
/* Creating the database if not exists */
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
/* Using the specified database */
USE hbtn_0d_usa;
/* Creating the table if not exists */
CREATE TABLE IF NOT EXISTS cities (
    id INT AUTO_INCREMENT PRIMARY KEY,
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    FOREIGN KEY (state_id) REFERENCES states(id)
);
