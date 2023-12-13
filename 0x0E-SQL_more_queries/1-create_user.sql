-- Script to create the MySQL server user user_0d_1
/* Creating the user if not exists */
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
/* Granting all privileges to the user */
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost' WITH GRANT OPTION;
