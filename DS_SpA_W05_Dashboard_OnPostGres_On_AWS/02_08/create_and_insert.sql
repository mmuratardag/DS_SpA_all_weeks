-- Delete the countries table if it already exists

DROP TABLE IF EXISTS countries;

-- Create Table
CREATE TABLE countries (

    id SERIAL PRIMARY KEY,
    country_name VARCHAR(50) NOT NULL,
    country_code CHAR(2) UNIQUE,
    population INTEGER NOT NULL,
    birth_rate REAL,
    capital_city VARCHAR(50)
    );

-- INSERT SOME DATA
-- INSERT INTO countries (country_name, country_code, population, birth_rate, capital_city) VALUES ('Germany', 'DE', 80000000, 1.5, 'Berlin');
-- INSERT INTO countries (country_name, country_code, population, birth_rate, capital_city) VALUES ('France', 'FR', 80000000, 1.5, 'Paris');
-- INSERT INTO countries (country_name, country_code, population, birth_rate, capital_city) VALUES ('United States', 'US', 350000000, 1.5, 'Washington, D.C.');

-- To run this script in psql, you can add the -f option: e.g.:
-- psql -h <hostname> -p 5432 -d <database_name> -U <username> -f create_and_insert.sql


INSERT INTO countries VALUES (DEFAULT, 'Germany', 'DE', 80000000, 1.5, 'Berlin');
INSERT INTO countries VALUES (DEFAULT, 'France', 'FR', 80000000, 1.5, 'Paris');
INSERT INTO countries VALUES (DEFAULT, 'United States', 'US', 350000000, 1.5, 'Washington, D.C.');
