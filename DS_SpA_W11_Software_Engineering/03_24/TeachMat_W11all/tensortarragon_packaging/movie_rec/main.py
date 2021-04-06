from rec_class import RecommenderClass
from subfolder.data import MOVIES


rec = RecommenderClass(MOVIES)
print(rec.recommend_movie())