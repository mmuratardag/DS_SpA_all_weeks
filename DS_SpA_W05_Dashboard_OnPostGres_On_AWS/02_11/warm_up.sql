
-- CREATE DATABASE dbname;

-- CREATE DATABASE singer_song;

CREATE TABLE singer (
   id SERIAL PRIMARY KEY,
   name VARCHAR(100)
   );

CREATE TABLE song (
   id INTEGER  PRIMARY KEY,
   name  CHARACTER VARYING(20),
   singer_id INTEGER,

   FOREIGN KEY(singer_id)
      REFERENCES singer(id) ON DELETE CASCADE
   );

\copy singer FROM './data/singer.csv' DELIMITER ',' CSV HEADER;

\copy song FROM './data/song.csv' DELIMITER ',' CSV HEADER;

