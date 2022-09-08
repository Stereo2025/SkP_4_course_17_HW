from flask import request, abort, jsonify
from flask_restx import Namespace, Resource
from generals.global_variables import db
from models_schemas_and_create_db.models import Director
from models_schemas_and_create_db.schemas import director_schema, directors_schema


directors_ns = Namespace('directors')


@directors_ns.route('/')
class DirectorsView(Resource):

    def get(self):

        director = Director.query.all()
        return directors_schema.dump(director)

    def post(self):

        query = request.json
        new_director = Director(**query)
        with db.session.begin():
            db.session.add(new_director)
        return 'The director has been successfully added to the database', 201


@directors_ns.route('/<int:uid>/')
class DirectorViews(Resource):

    def get(self, uid: int):

        director = Director.query.get(uid)
        if not director:
            abort(404)

        return director_schema.dump(director)

    def put(self, uid: int):

        director = Director.query.get(uid)
        if not director:
            abort(404)

        query = request.json
        director.name = query.get('name')
        db.session.add(director)
        db.session.commit()
        return jsonify({'Attention': f'Director №{uid} is update'})

    def patch(self, uid: int):

        director = Director.query.get(uid)
        if not director:
            abort(404)
        query = request.json

        if 'name' in query:
            director.name = query['name']
        db.session.add(director)
        db.session.commit()
        return jsonify({'Attention': f'Director №{uid} is update'})

    def delete(self, uid: int):

        director = Director.query.get(uid)
        if not director:
            abort(404)
        db.session.delete(director)
        db.session.commit()
        return jsonify({'Attention': f'Director №{uid} is delete'})
