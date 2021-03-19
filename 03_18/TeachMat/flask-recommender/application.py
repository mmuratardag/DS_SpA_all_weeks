
from flask import Flask, render_template, make_response, jsonify
from recommender import get_recommendation, MOVIES


app = Flask(__name__)

@app.route('/recommender') # <-- decorator
def recommend():
    movie = get_recommendation()
    return render_template('recommendation.html', 
          movie=movie, message="Hello World")

@app.route('/')
def main_page():
    return render_template('main_page.html')

@app.route('/all')
def all_movies():
    data = {'movies': MOVIES}
    return make_response(jsonify(data))


if __name__ == "__main__":
    # this block is executed when we run application.py, not when we import it
    app.run(debug=True, port=5000)
