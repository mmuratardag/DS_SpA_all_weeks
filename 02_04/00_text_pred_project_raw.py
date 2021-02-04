#!/usr/bin/env python
# coding: utf-8

# In[1]:


seed = 666

import pandas as pd
import numpy as np

import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split

from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import FunctionTransformer

from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import accuracy_score, precision_score, recall_score, confusion_matrix, f1_score

from time import time

import re, random

from nltk import word_tokenize, sent_tokenize, pos_tag
from nltk.util import ngrams
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import RegexpTokenizer

import spacy
nlp = spacy.load('en_core_web_sm', disable=['tagger', 'parser', 'ner'])



corpus_df = pd.read_csv('corpus_data.csv').drop(columns=['Unnamed: 0'])
corpus_df.head()



def lemma_w_sp(df):
    
    """Function that takes in a DF column ['lyrics'];
       returns lemmatized version of that column with spacy"""
    
    df = df.copy()
    
    df['lyrics'] = df['lyrics'].apply(lambda row: " ".join([w.lemma_ for w in nlp(row)]))
    
    return df



corpus_df = lemma_w_sp(corpus_df)
corpus_df.head()



X_train, X_test, y_train, y_test = train_test_split(corpus_df['lyrics'], corpus_df['genre'], test_size=.25, random_state=seed,
                                                    stratify=corpus_df['genre'])



vectoriser = TfidfVectorizer(token_pattern=r'[a-z]+', stop_words='english', min_df=10, max_df=.97)



X_train_pr = vectoriser.fit_transform(X_train)



m = RandomForestClassifier(max_depth=5, random_state=seed, n_jobs=-1)
m.fit(X_train_pr, y_train)
m.score(X_train_pr, y_train)



X_test_pr = vectoriser.transform(X_test)
pd.DataFrame(X_test_pr.todense(), columns=vectoriser.get_feature_names())



m.score(X_test_pr, y_test)


ypred_rf = m.predict(X_test_pr)
# print(f'The accuracy of the model is: {round(accuracy_score(y_test, ypred_rf), 3)}')
print(f'The precision using punk is: {round(precision_score(y_test, ypred_rf, average="binary", pos_label="punk"), 3)}')
print(f'The precision using indie is: {round(precision_score(y_test, ypred_rf, average="binary", pos_label="indie"), 3)}')
print(f'The recall of using punk is: {round(recall_score(y_test, ypred_rf, average="binary", pos_label="punk"), 3)}')
print(f'The recall of using indie is: {round(recall_score(y_test, ypred_rf, average="binary", pos_label="indie"), 3)}')
print(f'The f1-score using punk is: {round(f1_score(y_test, ypred_rf, average="binary", pos_label="punk"), 3)}')
print(f'The f1-score using indie is: {round(f1_score(y_test, ypred_rf, average="binary", pos_label="indie"), 3)}')



text_pipeline = make_pipeline(#FunctionTransformer(lemma_w_sp),
                              TfidfVectorizer(token_pattern=r'[a-z]+', stop_words='english', min_df=10, max_df=.97),
                              RandomForestClassifier(max_depth=5, random_state=seed, n_jobs=-1))
text_pipeline.fit(X_train, y_train)



text_pipeline.predict_proba(['Sometimes I give myself the creeps'])