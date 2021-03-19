
from flask import Flask, render_template, make_response, jsonify
from recommender import get_recommendations, movies


app = Flask(__name__)

@app.route('/recommender')
def recommend():
     top3 = get_recommendations()
     #movie = get_recommendations()
     return render_template('recommendation.html',
     top3 = top3)


@app.route('/')
def main_page():
     return render_template('main_page.html')


@app.route('/all')
def all_movies():
     data = {'movies': movies}
     return make_response(jsonify(data))


if __name__ == "__main__":
    app.run(debug=True, port=5000)