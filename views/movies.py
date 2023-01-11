
from flask_restx import Resource, Namespace
from flask import request
from container import movie_service
from service.decorators import admin_requred, auth_requered

movies_ns = Namespace('movies')


@movies_ns.route('/')
class MoviesView(Resource):
    
    @auth_requered
    def get(self):
        if request.args:
            return movie_service.get_movies_by_fields(), 200
        return movie_service.get_all_movies(), 200
        
    @admin_requred
    def post(self):
        return movie_service.add_movie(), 201
    

@movies_ns.route('/<int:mid>')
class MoviesView(Resource):
    
    @auth_requered
    def get(self, mid):
        return movie_service.get_movie_by_id(mid), 200
    
    @admin_requred
    def put(self, mid):
        return movie_service.put_movie(mid), 204
    
    @admin_requred
    def delete(self, mid):
        return movie_service.delete_movie(mid), 200
    

    
