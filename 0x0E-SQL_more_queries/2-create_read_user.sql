-- Script to create the database hbtn_0d_2 and the user user_0d_2
/* Creating the database if not exists */
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
/* Creating the user if not exists */
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
/* Granting privileges to the user */
GRANT USAGE ON *.* TO 'user_0d_2'@'localhost';
GRANT SELECT ON `hbtn_0d_2`.* TO 'user_0d_2'@'localhost';
