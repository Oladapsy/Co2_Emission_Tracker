-- Create a Mysql Server with:
-- Databse co2db
-- User oladapsy with password 1234 in localhost
-- Grand all privileges for oladapsy on co2db

CREATE DATABASE IF NOT EXISTS co2db;
CREATE USER
    IF NOT EXIST 'oladapsy'@'localhost'
    IDENTIFIED BY '1234';
GRANT ALL PRIVILEGES
    ON 'co2db'.*
    TO 'oladapsy'@'localhost'
    IDENTIFIED BY '1234';
FLUSH PRIVILEGES;
