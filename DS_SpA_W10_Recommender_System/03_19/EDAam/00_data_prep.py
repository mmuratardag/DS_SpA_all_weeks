import pandas as pd

movies =  pd.read_csv('data/movies.csv')
ratings = pd.read_csv('data/ratings.csv')

df = pd.merge(ratings, movies, how="left", on=["movieId"])
genres_expanded = df["genres"].str.split("|", n = 5, expand = True)
genres_expanded = genres_expanded.rename(columns={0: "Genre0", 1: "Genre1", 2:"Genre2", 3:"Genre3", 4:"Genre4", 5:"Genre5"})

df = pd.concat([df, genres_expanded], axis=1)
df = df.drop(['genres', 'timestamp'], axis=1)

df['title_only'] = df['title'].replace('\(.*', '', regex = True)
df = df[['userId', 'movieId', 'rating', 'title', 'title_only', 'Genre0', 'Genre1', 'Genre2', 'Genre3', 'Genre4', 'Genre5']]

df.to_csv('data/df.csv', index=False)