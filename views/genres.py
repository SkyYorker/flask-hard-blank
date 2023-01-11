from flask_restx import Resource, Namespace
from container import genre_service
from service.decorators import auth_requered

genres_ns = Namespace('genres')


@genres_ns.route('/')
class GenresView(Resource):
    
    @auth_requered
    def get(self):
        return genre_service.get_all_genres(), 200
    
    
@genres_ns.route('/<int:mid>')
class GenresView(Resource):
    
    @auth_requered
    def get(self, mid):
        return genre_service.get_genre_by_id(mid), 200