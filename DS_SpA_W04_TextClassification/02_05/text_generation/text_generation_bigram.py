"""
RUN
-----
>>> python text_generation_bigram.py

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

def bigram_word_distribution(data):
    """create a probability distribution over all bigrams
    
       params: data - a Bunch data object from sklearn
       returns: Word probability distribution
    """

    text = data['data']
    all_data = ' '.join([' '.join(re.findall('(?u)\\b\\w\\w+\\b',article.lower())) for article in text]).split()
    words = pd.DataFrame({'words':all_data})
    words['next_words'] = words['words'].shift(-1)
    word_distribution = words.groupby('words')['next_words'].value_counts(normalize=True)
    
    return word_distribution


def bigram_text_generation(seed, length, distribution):
    """seed a distribution with a seed word, and ask it to make more words
        
        params: seed - A seed word, 
                length -Length of the generated sentence
                distribution - A word probability distribution
                
        returns: generated sentence
    """
    
    try:
        seed = seed.lower()
        for i in range(length):
             seed += ' ' + np.random.choice(distribution[seed.split()[-1]].index, p=distribution[seed.split()[-1]].values)
        return seed
    
    except:
        print('Oops! Try another seed')
        return None
    
if __name__ == '__main__':
    
    #get data
    print('fetching data...\n')
    data = fetch_20newsgroups(remove=['headers', 'footers'])
    
    print('assembling transition probabilities...\n')
    bi_dist = bigram_word_distribution(data)
    
    seed = input('Enter starting word: ')
    sentence = bigram_text_generation('It', 20, bi_dist)
    

    attempts = []

    for i in range(10):
        bi = bigram_text_generation(seed,20,bi_dist)
        print(f'bigram: {bi}')
        attempts.append(bi)
        print()
    
    print('OK so maybe it doesn\'t make that much sense. Using Trigrams would make it better ')
