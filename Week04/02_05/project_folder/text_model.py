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

# import the DF
corpus_df = pd.read_csv('corpus_data.csv').drop(columns=['Unnamed: 0'])

# define the lemmatizer function
def lemma_w_sp(df):

    """Function that takes in a DF column ['lyrics'];
       returns lemmatized version of that column with spacy
       stop wors are also removed... I think
       if not, they are removed below"""

    df = df.copy()

    df['lyrics'] = df['lyrics'].apply(lambda row: " ".join([w.lemma_ for w in nlp(row)]))

    return df

# lemmatize the text column
corpus_df = lemma_w_sp(corpus_df)

# get corpus
CORPUS = list(corpus_df['lyrics'])

TEXT_CORPUS = CORPUS

# get labels
LABELS = list(corpus_df['genre'])

LABELS = LABELS


def train_model(text, labels, max_depth):
    """
    Takes in list of songs
    trains model on it with labels,
    and returns trained model
    """
    print('\nTraining model...')
    #cv = CountVectorizer(stop_words='english')
    tf = TfidfVectorizer(token_pattern=r'[a-z]+', stop_words='english', min_df=10, max_df=.97)
    rf = RandomForestClassifier(max_depth=20, random_state=666, n_jobs=-1)
    model = make_pipeline(tf, rf)
    model.fit(text, labels)
    print('...and done!\n')
    return model


def predict(pipeline, new_text):
    """
    Takes the pre-trained pipeline model and predicts new artist.
    """
    prediction = pipeline.predict(new_text)
    probs = pipeline.predict_proba(new_text)
    return prediction[0], probs.max()
