-- create table with country users
CREATE TABLE IF NOT EXISTS users (
        id INTEGER NOT NULL AUTO_INCREAMENT,
        email VARCHAR(255) NOT NULL UNIQUE,
        name VARCHAR(255),
        country ENUM('US', 'CO', 'TN') NOT NULL DEFAULT 'US'
);
