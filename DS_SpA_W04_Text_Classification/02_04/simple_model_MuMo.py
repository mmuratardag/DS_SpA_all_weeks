"""
example pipeline for building a CLI on top of it
"""
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.pipeline import make_pipeline
from sklearn.ensemble import RandomForestClassifier

ARTIST1 = 'Alt-J'
ARTIST2 = 'Abba'

TEXT_CORPUS = ['as the mind evolves menaces are born',
               'this is this is this is for matilda girl',
               'she may contain the urge to run away',
               'muscle to muscle toe to toe the fear has gripped me',
               'my heart sinks as i jump up your hand grips',
               'My, my, at Waterloo Napoleon did surrender',
               'Oh yeah, and I have met my destiny in quite a similar way',
               'The history book on the shelf is always repeating itself',
               'If you change your mind, Im the first in line',
               'Honey Im still free, take a chance on me',]

LABELS = [ARTIST1] * 5 + [ARTIST2] * 5

def train_model(text, labels, max_depth):
    """
    Takes in list of songs
    trains model on it with labels,
    and returns trained model
    """
    print('\nTraining model...')
    cv = CountVectorizer(stop_words='english')
    tf = TfidfTransformer()
    rf = RandomForestClassifier(max_depth=max_depth)
    model = make_pipeline(cv, tf, rf)
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
