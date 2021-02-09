
DROP TABLE penguins CASCADE;
DROP TABLE flippers;

CREATE TABLE penguins (
     species VARCHAR(20),
     culmen_length NUMERIC,
     culmen_depth NUMERIC,
     flipper_length NUMERIC,
     body_mass NUMERIC,
     gender VARCHAR(10)
);

\copy penguins FROM '/home/kristian/projects/tensor-tarragon-encounter-notes/week_01/penguins_simple.csv' CSV HEADER DELIMITER ';'

SELECT species, gender, avg(flipper_length) mean, count(species) n_penguins
  FROM penguins
  WHERE flipper_length <= 190.0
  GROUP BY species, gender
  HAVING count(species) > 10 
  OFFSET 1   
  LIMIT 5;



CREATE TABLE flippers AS (SELECT species, gender, avg(flipper_length) mean, count(species) n_penguins
  FROM penguins
  WHERE flipper_length <= 190.0
  GROUP BY species, gender
  HAVING count(species) > 10 
  OFFSET 1   
  LIMIT 5);


\copy flippers TO '/home/kristian/flippers.csv' CSV HEADER DELIMITER ';'

