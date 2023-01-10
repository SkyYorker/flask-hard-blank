from flask import request
from .model.directors import Director, director_schema, directors_schema
from setup_db import db

class DirectorDAO:
    def get_all_directors(self):
        all_directors = Director.query.all()
        return directors_schema.dump(all_directors)
    
    def get_director_by_id(self, did):
        director = Director.query.get(did)
        return director_schema.dump(director)
    
    def add_director(self):
        req_json = request.json
        new_director = Director(**req_json)
        with db.session.begin():
            db.session.add(new_director)
        return ""
    
    def put_director(self, did):
        director = Director.query.get(did)
        req_json = request.json
        director.name = req_json.get('name')
        db.session.add(director)
        db.session.commit()
        return ""
    
    def delete_director(self, did):
        director = Director.query.get(did)
        db.session.delete(director)
        db.session.commit()
        return ""
        