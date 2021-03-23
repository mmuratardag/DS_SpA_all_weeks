
import pandas as pd

movies =  pd.read_csv('data/movies.csv')
ratings = pd.read_csv('data/ratings.csv')

df = pd.merge(ratings, movies, how="left", on=["movieId"])
genres_expanded = df["genres"].str.split("|", n = 5, expand = True)
genres_expanded = genres_expanded.rename(columns={0: "Genre0", 1: "Genre1", 2:"Genre2", 3:"Genre3", 4:"Genre4", 5:"Genre5"})

df = pd.concat([df, genres_expanded], axis=1)
df = df.drop('genres', axis=1)
df.to_csv('data/df.csv', index=False)

