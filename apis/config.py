from flask import Flask
from flask_restx import Api
from raw_data.import_sql import db
from apis.movie_namespace import movies_ns
from apis.genre_namespace import genres_ns
from apis.director_namespace import directors_ns

app = Flask(__name__)
app.app_context().push()
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../HW_17.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json_ensure_ascii = False

db.init_app(app)

api = Api(app)
api.app.config['RESTX_JSON'] = {'ensure_ascii': False, 'indent': 4}

api.add_namespace(movies_ns)
api.add_namespace(genres_ns)
api.add_namespace(directors_ns)
