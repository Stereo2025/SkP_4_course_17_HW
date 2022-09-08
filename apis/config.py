from flask import Blueprint
from flask_restx import Api
from apis.movie_namespace import movies_ns
from apis.genre_namespace import genres_ns
from apis.director_namespace import directors_ns


blue_print = Blueprint('api', __name__)
api = Api(blue_print)


api.add_namespace(movies_ns)
api.add_namespace(genres_ns)
api.add_namespace(directors_ns)
