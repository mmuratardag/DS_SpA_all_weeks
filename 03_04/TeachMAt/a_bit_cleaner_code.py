import random

STATES = [
'airport', 'air', 'crashed'
]

def mcmc(i, P):
    the_list = [i]
    s = i
    while s!='crashed':
        probs = P[s]
        s = random.choices(STATES, probs) [0]
        the_list.append(s)
        if the_list[-1] == 'crashed':
            return list

P = {
    'airport': [0.4, 0.6, 0.0],
    'air': [0.8, 0.19999, 0.00001],
}
print(f"crashed after {len(mcmc('airport', P))} days of service")
