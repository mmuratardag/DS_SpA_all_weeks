#!/usr/bin/env python

import random

MOVIES = [
    "The Green Book",
    "Django",
    "Hors de prix"
]

def get_recommendation():
    return random.choice(MOVIES)



if __name__ == '__main__':
    """good place for test code"""
    print('HELLO TENSORS!')
    movie = get_recommendation()
    print(movie)
