-- Creates a table called users.
CREATE TABLE IF NOT EXISTS users (
	id INT AUTO_INCREAMENT PRIMARY KEY,
	email VARCHAR(255) NOT NULL UNIQUE,
	name VARCHAR(255)
);