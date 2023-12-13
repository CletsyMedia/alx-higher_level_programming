-- Script to create the table unique_id
/* Using the specified database hbtn_0d_2 */
/* Creating the table if not exists */
CREATE TABLE IF NOT EXISTS unique_id (
    id INT DEFAULT 1 UNIQUE,
    name VARCHAR(256)
);
