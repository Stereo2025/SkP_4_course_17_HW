from flask import request, abort, jsonify
from flask_restx import Namespace, Resource
from generals.global_variables import db
from models_schemas_and_create_db.models import Genre
from models_schemas_and_create_db.schemas import genre_schema, genres_schema


genres_ns = Namespace('genres')


@genres_ns.route('/')
class GenresViews(Resource):

    def get(self):

        genres = Genre.query.all()
        return genres_schema.dump(genres), 200

    def post(self):

        query = request.json
        new_genre = Genre(**query)
        with db.session.begin():
            db.session.add(new_genre)
        return 'The genre has been successfully added to the database', 201


@genres_ns.route('/<int:uid>/')
class GenreViews(Resource):

    def get(self, uid: int):

        genre = Genre.query.get(uid)
        if not genre:
            abort(404)

        return genre_schema.dump(genre)

    def put(self, uid: int):

        genre = Genre.query.get(uid)
        if not genre:
            abort(404)

        query = request.json
        genre.name = query.get('name')
        db.session.add(genre)
        db.session.commit()
        return jsonify({'Attention': f'Genre №{uid} is update'})

    def patch(self, uid: int):

        genre = Genre.query.get(uid)
        if not genre:
            abort(404)
        query = request.json

        if 'name' in query:
            genre.name = query['name']
        db.session.add(genre)
        db.session.commit()
        return jsonify({'Attention': f'Genre №{uid} is update'})

    def delete(self, uid: int):

        genre = Genre.query.get(uid)
        if not genre:
            abort(404)
        db.session.delete(genre)
        db.session.commit()
        return jsonify({'Attention': f'Genre №{uid} is delete'})
