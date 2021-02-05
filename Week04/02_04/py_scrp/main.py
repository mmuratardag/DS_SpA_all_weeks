"""Main file for our artist-prediction-program"""
import argparse
from simple_model import predict, train_model, TEXT_CORPUS, LABELS


# 1. Option: very simple way of getting input from the terminal
#user_input = input("Please enter the text for the prediction: \n")


# 2. Option: a bit more advanced
parser = argparse.ArgumentParser(description='This program predicts the artist of a given text.')  #Initialization
parser.add_argument('given_text', help="Give the text that is th einput for the presiction as a string")
parser.add_argument('--md', '-max_depth', type=int, default=7, help='Give the max.depth that the RandomForest should be trained with')   #choices
# add as many arguments as you like 
args = parser.parse_args()


m = train_model(TEXT_CORPUS, LABELS, args.md)
prediction, probs = predict(m, [args.given_text])
print(prediction, probs)