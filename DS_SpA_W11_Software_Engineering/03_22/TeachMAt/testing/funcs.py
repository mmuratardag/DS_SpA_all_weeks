"""Simple Functions to practice testing and handling errors"""
import random


def add_one(x):
    result = x + 1
    return result


def recommend_movie(movie_list):
    try: 
        rec = random.choice(movie_list)
        return(rec.upper())
    except IndexError: 
        return('Oops please try again and put in some movies.')

#recommend_movie([])


def first_letter(text):
    if type(text) != str: 
        raise TypeError('The input has to be a string.')
    print(text[0])