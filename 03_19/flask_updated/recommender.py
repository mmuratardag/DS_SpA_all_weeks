#!/usr/bin/env python

import random
import pandas as pd

df = pd.read_csv('movie_titles_df.csv')

MOVIES = list(df['title_only'])

def get_three_random_recommendations():
    random.shuffle(MOVIES)
    return MOVIES[:3]


def get_nine_random_recommendations():
    random.shuffle(MOVIES)
    return MOVIES[:9]


def get_rating_from_user(user_input: dict):

    """The rest is up to you....HERE IS SOME PSEUDOCODE:
    
       1. Train the model (NMF), OR the model is already pre-trained.
       2. Process the input, e.g. convert movie titles into numbers: movie title -> column numbers
       3. Data validation, e.g. spell check....
       4. Convert the user input into an array of length len(df.columns), ~9742

       --here is where the cosine similarity will be a bit different--

       5. user_profile = nmf.transform(user_array). The "hidden feature profile" of the user, e.g. (9742, 20)
       6. results = np.dot(user_profile, nmf.components_)
       7. Sort the array, map the top N values to movie names.
       8. Return the titles. 
    """

    return random.choice(list(user_input.keys()))


if __name__ == "__main__":
    """good place for test code"""
    print("HELLO TENSORS!")
