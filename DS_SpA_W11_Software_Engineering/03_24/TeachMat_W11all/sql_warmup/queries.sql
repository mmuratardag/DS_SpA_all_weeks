---------------------------------------------------------------------------------------------------
-- Get all ratings since 2018
---------------------------------------------------------------------------------------------------
SELECT 
ratings.user_id,
ratings.movie_id,
ratings.rating
FROM ratings
WHERE ratings.timestamp >= '2018-01-01';

-- or simply the average rating:
SELECT 
AVG(rating)
FROM ratings
WHERE ratings.timestamp >= '2018-01-01';

---------------------------------------------------------------------------------------------------
-- Display the names of movies that have been rated the most (top 5)
---------------------------------------------------------------------------------------------------
SELECT 
    movies.movie_id,
    movies.title,
COUNT(ratings.user_id) AS total_ratings

FROM
    movies
JOIN 
    ratings
ON 
    ratings.movie_id = movies.movie_id

GROUP BY 
    movies.movie_id, movies.title
ORDER BY 
    total_ratings DESC
LIMIT 5;

---------------------------------------------------------------------------------------------------
-- Combine the 2, i.e. Display the names of movies that have been rated the most since 2018
---------------------------------------------------------------------------------------------------

WITH ratings_2018 AS (
SELECT 

    ratings.user_id,
    ratings.movie_id,
    ratings.rating
    
FROM ratings
WHERE ratings.timestamp >= '2018-01-01'
)

SELECT 
    movies.movie_id,
    movies.title,
    COUNT(ratings_2018.user_id) AS total_ratings

FROM
    movies
JOIN 
    ratings_2018
ON 
    ratings_2018.movie_id = movies.movie_id

GROUP BY 
    movies.movie_id, movies.title
ORDER BY 
    total_ratings DESC
LIMIT 5;


---------------------------------------------------------------------------------------------------
-- Elevator Weight Problem
-- People are queueing for a lift with a maximum weight capacity of 1000 lb.
-- Write a query that will return the full name of the last person that will be able to
-- board the lift without exceeding the maximum load.
---------------------------------------------------------------------------------------------------

SELECT position, cumulative_weight, first_name || ' ' || last_name AS full_name

FROM (

-- window function for cumulative sum!
SELECT first_name, last_name, position, 
    sum(weight) OVER (ORDER BY position) as cumulative_weight
FROM elevator
ORDER BY position
) AS cumulative

WHERE cumulative_weight < 1000

ORDER BY position DESC
LIMIT 1;
