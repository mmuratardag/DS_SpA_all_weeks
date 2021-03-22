from flask import Flask, render_template, make_response, jsonify, request
from recommender import get_recommendation, MOVIES


app = Flask(__name__)


@app.route("/recommender")  # <-- decorator
def recommend():

    user_input = dict(request.args)
    ### THIS IS THE DATA THAT WAS ASSEMBLED BY THE FORM!!!

    movie = get_recommendation(user_input)
    return render_template("recommendation.html", movie=movie, message="Hello World")


@app.route("/")
def main_page():
    return render_template("main_page.html")


@app.route("/all")
def all_movies():
    data = {"movies": MOVIES}
    return make_response(jsonify(data))


@app.route("/greet/<name>")
def hello(name):
    return f"Hello, {name}"


@app.route("/api/<movie1>&<movie2>&<movie3>")
def simple_recommender(movie1, movie2, movie3):

    """We can basically make our own API using Flask dynamic
    arguments"""

    data = {
        "your_input": [movie1, movie2, movie3],
        # "recommendation": nmf_recommender(movie1, movie2, movie3),
        # ^^^ Ultimately what we want!!
        # i.e. a function that makes predictions BASED ON user input!!!
        "recommendation": get_recommendation(),
    }

    return make_response(jsonify(data))


if __name__ == "__main__":
    # this block is executed when we run application.py, not when we import it
    app.run(debug=True, port=5000)
