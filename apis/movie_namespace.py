from flask import request, abort, jsonify
from flask_restx import Namespace, Resource
from generals.global_variables import db
from models_schemas_and_create_db.models import Movie
from models_schemas_and_create_db.schemas import movies_schema, movie_schema


movies_ns = Namespace('movies')


@movies_ns.route("/")
class MoviesView(Resource):

    def get(self):

        movies = Movie.query.all()
        director_id = request.args.get('director_id')
        genre_id = request.args.get('genre_id')

        if director_id:
            movies = Movie.query.filter(Movie.director_id == director_id)
        elif genre_id:
            movies = Movie.query.filter(Movie.genre_id == genre_id)
        query = movies

        return movies_schema.dump(query), 200

    def post(self):

        query = request.json
        new_movie = Movie(**query)
        with db.session.begin():
            db.session.add(new_movie)
        return 'The movie has been successfully added to the database', 201


@movies_ns.route('/<int:uid>/')
class MovieView(Resource):

    def get(self, uid: int):

        movie = Movie.query.get(uid)
        if not movie:
            abort(404)
        return movie_schema.dump(movie)

    def put(self, uid: int):

        movie = Movie.query.get(uid)
        if not movie:
            abort(404)

        query = request.json
        movie.title = query.get('title')
        movie.description = query.get('description')
        movie.trailer = query.get('trailer')
        movie.year = query.get('year')
        movie.rating = query.get('rating')
        movie.genre_id = query.get('genre_id')
        movie.director_id = query.get('director_id')
        db.session.add(movie)
        db.session.commit()
        return jsonify({'Attention': f'Movie №{uid} is update'})

    def patch(self, uid: int):

        movie = Movie.query.get(uid)
        if not movie:
            abort(404)

        query = request.json
        if 'title' in query:
            movie.title = query['title']
        if 'description' in query:
            movie.description = query['description']
        if 'trailer' in query:
            movie.trailer = query['trailer']
        if 'year' in query:
            movie.year = query['year']
        if 'rating' in query:
            movie.rating = query['rating']
        if 'genre_id' in query:
            movie.genre_id = query['genre_id']
        if 'director_id' in query:
            movie.director_id = query['director_id']
        db.session.add(movie)
        db.session.commit()
        return jsonify({'Attention': f'Movie №{uid} is update'})

    def delete(self, uid: int):

        movie = Movie.query.get(uid)
        if not movie:
            abort(404)

        db.session.delete(movie)
        db.session.commit()
        return jsonify({'Attention': f'Movie №{uid} is delete'})
