Here are the credentials:

```
USERNAME = "postgres"
PASSWORD = "titanic99"
HOST = "recap.cgn1yvegh1gq.eu-central-1.rds.amazonaws.com"
PORT = "5432"
DB = "postgres"
```

**Connect to the database using any client you prefer**. I personally like graphical clients, e.g. Postico, PgAdmin4. Once you are connected, you will find 3 pre-filled tables:

1. `movies`
2. `ratings`
3. `elevator`





Connect to the database:

psql -h [recap.cgn1yvegh1gq.eu-central-1.rds.amazonaws.com](http://recap.cgn1yvegh1gq.eu-central-1.rds.amazonaws.com/) -p 5432 -U postgres -d postgres

[13:01](https://tensortarragon.slack.com/archives/D01HJ9730GP/p1616587273000400)

password is titanic99



Task 1: 

Using just the ratings table, calculate the average rating of all movies that have been rated since January 1, 2018.

Solutions:

-- 1 --
SELECT AVG (rating)
FROM ratings;

-- 2 --

SELECT AVG(rating) FROM PUBLIC.RATINGS where timestamp > '2018-01-01';

-- 3 --

SELECT AVG(rating) AS ratings_mean
FROM ratings
WHERE timestamp >= TO_TIMESTAMP( '2000-01-01', 'yyyy-mm-dd' )





Task 2:

Using both the ratings and movies tables, display the names of the movies that have been rated the most number of times.

Solutions:

-- 1 --

SELECT movies.title,
COUNT(ratings.rating)
FROM ratings, movies
WHERE ratings.movie_id=movies.movie_id
GROUP BY ratings.rating, movies.title
ORDER BY COUNT(rating) DESC;

-- 2 --

SELECT title, count(rating)
FROM ratings
INNER JOIN movies ON ratings.movie_id = movies.movie_id
GROUP BY rating, title
ORDER by count(ratings) desc;



Task 3:

Using both the ratings and movies tables, display the names of the movies that have been rated the most number of times since 2018 only.

Solutions:



Task 4:

Background: this was an SQL question that a former Spiced student got during a technical challenge.

Using the elevator table: People are queueing for a lift with a maximum weight capacity of 1000 lb. Write a query that will return the full name of the last person that will be able to board the lift without exceeding the maximum load.

Hint: this requires something called a "window function".

Solutions:

