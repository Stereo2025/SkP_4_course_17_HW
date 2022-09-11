from raw_data.import_sql import db
from raw_data.data_dict import data
from data_management.models import Movie, Director, Genre
from app import app


for movie in data["movies"]:
    _movie_ = Movie(
        id=movie["pk"],
        title=movie["title"],
        description=movie["description"],
        trailer=movie["trailer"],
        year=movie["year"],
        rating=movie["rating"],
        genre_id=movie["genre_id"],
        director_id=movie["director_id"],
    )
    with db.session.begin():
        db.session.add(_movie_)

for director in data["directors"]:
    _director_ = Director(
        id=director["pk"],
        name=director["name"],
    )
    with db.session.begin():
        db.session.add(_director_)

for genre in data["genres"]:
    _genre_ = Genre(
        id=genre["pk"],
        name=genre["name"],
    )
    with db.session.begin():
        db.session.add(_genre_)

db.session.commit()
