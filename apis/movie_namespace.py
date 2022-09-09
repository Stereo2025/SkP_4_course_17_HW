from flask import request, abort, jsonify
from flask_restx import Namespace, Resource
from generals.global_variables import db
from models_schemas_and_create_db.models import Movie
from models_schemas_and_create_db.schemas import movies_schema, movie_schema


movies_ns = Namespace('movies')


@movies_ns.route("/page=1/")
class MoviesView(Resource):

    # def get(self):
    #     """Функция возвращает все 'movie' из файла generals/data_dict."""
    #
    #     movies = Movie.query.all()
    #     director_id = request.args.get('director_id')
    #     genre_id = request.args.get('genre_id')
    #
    #     if director_id:
    #         movies = Movie.query.filter(Movie.director_id == director_id)
    #     elif genre_id:
    #         movies = Movie.query.filter(Movie.genre_id == genre_id)
    #     query = movies
    #
    #     return movies_schema.dump(query), 200
    def get(self):
        """Функция возвращает все 'movie' из файла generals/data_dict."""

        page = request.args.get('page', 1)
        items_per_page = 5

        movies = Movie.query
        director_id = request.args.get('director_id')
        genre_id = request.args.get('genre_id')

        if director_id:
            movies = Movie.query.filter(Movie.director_id == director_id)
        elif genre_id:
            movies = Movie.query.filter(Movie.genre_id == genre_id)

        movies = movies.paginate(page, items_per_page, error_out=False)

        return movies_schema.dump(movies.items), 200

    def post(self):
        """Функция добавляет 'movie' в файл data_dict. """

        query = request.json
        new_movie = Movie(**query)
        with db.session.begin():
            db.session.add(new_movie)
        return 'The movie has been successfully added to the database', 201


@movies_ns.route('/<int:uid>/')
class MovieView(Resource):

    def get(self, uid: int):
        """Функция показывает один 'movie' по выбранному id. Иначе 404"""

        movie = Movie.query.get(uid)
        if not movie:
            abort(404)
        return movie_schema.dump(movie)

    def put(self, uid: int):
        """Функция изменит данные выбранного по id 'movie' Put - обновляет объект целиком"""

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
        """Функция изменит данные выбранного по id 'movie' Patch - обновляет объект частично"""

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
        """Удаляет 'movie' по его id"""

        movie = Movie.query.get(uid)
        if not movie:
            abort(404)

        db.session.delete(movie)
        db.session.commit()
        return jsonify({'Attention': f'Movie №{uid} is delete'})
