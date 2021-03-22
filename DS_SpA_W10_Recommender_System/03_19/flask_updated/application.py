from flask import Flask, render_template, make_response, jsonify, request
from recommender import MOVIES, get_rating_from_user, get_three_random_recommendations, get_nine_random_recommendations, get_convert_user_input


app = Flask(__name__)


random3 = get_three_random_recommendations()
random9_2b_rated = get_nine_random_recommendations()

@app.route("/recommender")  # <-- decorator
def recommend():

    user_input = dict(request.args)
    ### THIS IS THE DATA THAT WAS ASSEMBLED BY THE FORM!!!
    print(user_input)
    movie = get_rating_from_user(user_input)
    test_df_var = get_convert_user_input(user_input)
    #test_df_var = str(test_df_var)
    test_df_var = print(test_df_var.to_string())
    return render_template("recommendation.html", movie = movie, message="test message", test_df_var = test_df_var)


@app.route("/")
def main_page():
    return render_template("main_page.html", random3 = random3, random9_2b_rated = random9_2b_rated)


#@app.route("/all")
#def all_movies():
#    data = {"movies": MOVIES}
#    return make_response(jsonify(data))


#@app.route("/greet/<name>")
#def hello(name):
#    return f"Hello, {name}"


@app.route("/api/<movie1>&<movie2>&<movie3>")
def simple_recommender(movie1, movie2, movie3):

    """We can basically make our own API using Flask dynamic
    arguments"""

    data = {
        "your_input": [movie1, movie2, movie3],
        # "recommendation": nmf_recommender(movie1, movie2, movie3),
        # ^^^ Ultimately what we want!!
        # i.e. a function that makes predictions BASED ON user input!!!
        "recommendation": get_rating_from_user(),
    }

    return make_response(jsonify(data))

#@app.route("/test")
#def test_get_user():
#    test_user_input_df = get_user_input()
#    print(test_user_input_df)


if __name__ == "__main__":
    # this block is executed when we run application.py, not when we import it
    app.run(debug=True, port=5000)
