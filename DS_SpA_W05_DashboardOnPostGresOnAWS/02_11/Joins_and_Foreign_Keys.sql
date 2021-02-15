DROP TABLE song;

-- Create the table singer
CREATE TABLE singer (
id SERIAL PRIMARY KEY,
name TEXT
);

-- Insert data into the table
INSERT INTO singer (name) VALUES ('Nicki Minaj'), ('Lady Gaga'), ('Taylor Swift'), ('Tom Jones');


-- Create Table song
CREATE TABLE song (
   id SERIAL PRIMARY KEY,
   name  CHARACTER VARYING(20),
   singer_id INTEGER REFERENCES singer (id)
   );
   
-- Insert Data into the table song
INSERT INTO song VALUES (1, 'Anaconda', 1), (2, 'Paparazzi', 2), (3, 'Bad Romance', 2), (4, 'Sex Bomb', 4);


-- Question: What songs did Lady Gaga sing?
-- In order to retrieve this information, we need data from several tables - Join tables
-- How do we know which tables to join to get to the information we are interested in? - Give tables descriptive names
-- We have to understand the relation between tables
SELECT singer.name as artist, song.name as songname
FROM song
JOIN singer ON singer.id = song.singer_id
WHERE singer.name = 'Lady Gaga';


-- Different types of joins - Inner Join, (Full) Outer Join, Left (Outer) Join, Right (Outer) Join (, Cross Join, Self Join)

-- Inner Join - results in all observations that exist in both tables
SELECT *
FROM song
INNER JOIN singer ON singer.id = song.singer_id;


-- Full Outer Join - results in all observations that exist in both tables
SELECT *
FROM song
FULL JOIN singer ON singer.id = song.singer_id;


-- Left (Outer) Join - results in all observations from the first table and only the corresponding ones from the second table
SELECT *
FROM song
LEFT JOIN singer ON singer.id = song.singer_id;


-- Right (Outer) Join - results in all observations from the second table and only the corresponding ones from the first table
SELECT *
FROM song
RIGHT JOIN singer ON singer.id = song.singer_id;


-- Cross Join connects every entry from the first table with every entry from the second table
SELECT *
FROM song
CROSS JOIN singer;


-- Let us create a new song
INSERT INTO song VALUES (5, 'Yesterday', NULL); -- This will not work due to the Foreign Key constraint


-- Adding Constraing
ALTER TABLE song
ALTER COLUMN singer_id SET NOT NULL;





