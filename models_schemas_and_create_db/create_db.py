from generals.global_variables import db
from generals.data_dict import data
from models_schemas_and_create_db.models import Movie, Director, Genre


def create_dbase():

    db.drop_all()
    db.create_all()

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
