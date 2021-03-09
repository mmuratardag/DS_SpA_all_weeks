"""
Useful python linters:
To help you conform to the so-called "PEP 8" style guide.
- pylint (most manual) 
- flake8 (similar to pylint, can also be used as an IDE extension)
- autopep8 (similar to flake8)
- black (totally automated)
- isort (cherry on top)
"""
import random
import time
import typing
import faker
import pandas as pd
from sklearn.linear_model import (
    ElasticNet,
    Lasso,
    LinearRegression,
    LogisticRegression,
    Ridge,
)
STATES = ["airport", "air", "crashed"]
def mcmc(i, transition_dict):
    my_list = [i]
    s = i
    while s != "crashed":
        probs = transition_dict[s]
        s = random.choices(STATES, probs)[0]
        my_list.append(s)
        if my_list[-1] == "crashed":
            return my_list
P = {
    "airport": [0.4, 0.6, 0.0],
    "air": [0.8, 0.19999, 0.00001],
}
print(f"crashed after {len(mcmc('airport', P))} days of service")