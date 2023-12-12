-- Convert the hbtn_0c_0 database and first_table table to UTF8
USE `hbtn_0c_0`;
ALTER DATABASE CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
ALTER TABLE `first_table` CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
