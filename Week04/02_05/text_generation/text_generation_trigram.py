"""
RUN
-----
>>> python text_generation_trigram.py

ABOUT
-----
A 'traditional' language model for text sequence generation: A trigram Markov chain using pandas and numpy.

No neural networks required :)

The first time you run this code it will download the 20newsgroup text data.

How to improve:
    - Monitor sentence start distributions differently
    - Add start and end tokens to generate separable sentences
    - Add other punctuation
"""


from sklearn.datasets import fetch_20newsgroups
import pandas as pd
import numpy as np
import re

def trigram_word_distribution(data):
    """create a probability distribution over all trigrams
    
        params: data - a Bunch data object from sklearn
        returns: [Bigram probability distribution, trigram probability distribution]
    """
    
    text = data['data']
    all_data = ' '.join([' '.join(re.findall('(?u)\\b\\w\\w+\\b',article.lower())) for article in text]).split()
    tri_gram = [' '.join([x,y]) for x,y in zip(all_data[:-1:], all_data[1::])]
    next_word = all_data[2:] + [' '] * 1
    words = pd.DataFrame({'seed_word':all_data[:-1],'gram_words':tri_gram, "next_word":next_word})
    words['seed_next_word'] = words['seed_word'].shift(-1)
    seed_word_distribution = words.groupby('seed_word')['seed_next_word'].value_counts(normalize=True)
    gram_word_distribution = words.groupby('gram_words')['next_word'].value_counts(normalize=True)
    
    return [seed_word_distribution, gram_word_distribution]


def trigram_text_generation(seed, length, distribution):
    """seed a distribution with a seed word, and ask it to make more words
        
        params: seed - A seed word, 
                length -Length of the generated sentence
                distribution - A word probability distribution
                
        returns: generated sentence
    """
    
    try:
        seed = seed.lower()
        seed += ' ' + np.random.choice(distribution[0][seed].index, p=distribution[0][seed].values)
        for i in range(length):
             seed += ' ' + np.random.choice(distribution[1][' '.join(seed.split()[-2:])].index, p=distribution[1][' '.join(seed.split()[-2:])].values)
        return seed
    
    except:
        print('Oops! Try another seed')
        return None
    
if __name__ == '__main__':
    
    #get data
    print('fetching data...\n')
    data = fetch_20newsgroups(remove=['headers', 'footers'])
    
    print('assembling transition probabilities...\n')
    tri_dist = trigram_word_distribution(data)
    
    seed = input('Enter starting word: ')
    sentence = trigram_text_generation('It', 20, tri_dist)
    

    attempts = []

    for i in range(10):
        tri = trigram_text_generation(seed,20,tri_dist)
        print(f'bigram: {tri}')
        attempts.append(tri)
        print()
    

