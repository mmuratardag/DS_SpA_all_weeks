#!/usr/bin/env python

import random

MOVIES = ["The Green Book", "Django", "Hors de prix"]

# def get_recommendation():
#     return random.choice(MOVIES)


def get_recommendation(user_input: dict):

    m1 = user_input["movie1"]
    r1 = user_input["rating1"]

    m2 = user_input["movie2"]
    r2 = user_input["rating2"]

    m3 = user_input["movie3"]
    r3 = user_input["rating3"]

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

    return random.choice([m1, m2, m3])


if __name__ == "__main__":
    """good place for test code"""
    print("HELLO TENSORS!")
    movie = get_recommendation()
    print(movie)
