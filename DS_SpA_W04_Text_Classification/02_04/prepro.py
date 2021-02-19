#!/usr/bin/env python
# coding: utf-8

# In[1]:


seed = 666

import pandas as pd
import numpy as np

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split

from time import time

import re, random

from nltk import word_tokenize, sent_tokenize, pos_tag
from nltk.util import ngrams
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import RegexpTokenizer


# In[2]:


corpus_df = pd.read_csv('corpus_df.csv').drop(columns=['Unnamed: 0'])
corpus_df.head()
# corpus_df.shape # (1693, 3)


# In[3]:


# corpus_df['genre'].value_counts()
# punk     1097
# indie     596


# In[4]:


X_train, X_test, y_train, y_test = train_test_split(corpus_df['lyrics'], corpus_df['genre'], test_size=.25, random_state=seed, stratify=corpus_df['genre'])
# train = pd.concat([X_train, y_train], axis=1)
# test = pd.concat([X_test, y_test], axis=1)
X_train.shape, X_test.shape, y_train.shape, y_test.shape


# In[5]:


# train['genre'].value_counts()
# punk     822
# indie    447

# test['genre'].value_counts()
# punk     275
# indie    149


# In[6]:


def inspect(vectoriser, X):
    # Fit and transform
    start = time()
    print(f"There are {vectoriser.fit_transform(X).shape[1]} columns.\n")
    end = time()
    print(f"Took {round((end-start),2)} seconds.\n")
    
    # Inspect tokens
    tokens = list(vectoriser.vocabulary_.keys())
    tokens.sort()
    print(f"Example tokens: {tokens[:50]}\n")
    
    # Inspect ignored tokens
    ignored = vectoriser.stop_words_
    if len(ignored)==0:
        print("No token is ignored.")
    elif len(ignored)>50:
        print(f"Example ignored tokens: {random.sample(ignored, 50)}")
    else:
        print(f"Example ignored tokens: {ignored}")


# In[7]:


vectoriser = TfidfVectorizer(token_pattern=r'[a-z]+', stop_words='english', min_df=10, max_df=.97)
inspect(vectoriser, X_train)


# In[8]:


X = vectoriser.fit_transform(X_train)
X


# In[9]:


pd.DataFrame(X.todense(), columns=vectoriser.get_feature_names())


# In[10]:


# def preprocess_text(text):
#     # 1. Tokenise to alphabetic tokens
#     tokeniser = RegexpTokenizer(r'[A-Za-z]+')
#     tokens = tokeniser.tokenize(text)
    
#     # 2. POS tagging
#     pos_map = {'J': 'a', 'N': 'n', 'R': 'r', 'V': 'v'}
#     pos_tags = pos_tag(tokens)
    
#     # 3. Lowercase and lemmatise 
#     lemmatiser = WordNetLemmatizer()
#     tokens = [lemmatiser.lemmatize(t.lower(), pos=pos_map.get(p[0], 'v')) for t, p in pos_tags]

#     return tokens


# In[11]:


# vectoriser = TfidfVectorizer(analyzer=preprocess_text, min_df=10, max_df=.97)
# X = vectoriser.fit_transform(X_train)
# X

