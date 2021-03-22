
import random
import pandas as pd

df = pd.read_csv('movie_titles_df.csv')

movies = list(df['title_only'])

def get_recommendations():
    random.shuffle(movies)
    return movies[:3]

if __name__ == '__main__':
    movie = get_recommendations()
    print(movie)