import random


class RecommenderClass:
    """Class for grouping all my recommender-functions"""
    
    def __init__(self, movie_list:list):   #type annotation
        self.movies = movie_list # attribute
        
    def recommend_movie(self):
        """Randomly recommend one movie from a given list."""
    
        result = random.choice(self.movies)
        return result 

    def nmf(self):
        """Coming soon in version 2.0"""
        pass 



if __name__ == '__main__':
    c = RecommenderClass(MOVIES)
    print(c.recommend_movie())
    #print(__name__)




