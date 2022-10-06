from flask_restx import Resource, Namespace
from dao.directors import DirectorDAO
from container import director_service

directors_ns = Namespace('directors')


@directors_ns.route('/')
class DirectorsView(Resource):
    def get(self):
        return director_service.get_all_directors(), 200
    
    
@directors_ns.route('/<int:mid>')
class DirectorsView(Resource):
    def get(self, mid):
        return director_service.get_director_by_id(mid), 200
    