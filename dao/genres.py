from .model.genres import Genre, genres_schema, genre_schema
from flask import request
from setup_db import db

class GenreDAO:
    def get_all_genres(self):
        all_genres = Genre.query.all()
        return genres_schema.dump(all_genres)
    
    def get_genre_by_id(self, gid):
        genre = Genre.query.get(gid)
        return genre_schema.dump(genre)
    
    def add_genre(self):
        req_json = request.json
        new_genre = Genre(**req_json)
        with db.session.begin():
            db.session.add(new_genre)
        return ""
    
    def put_genre(self, gid):
        genre = Genre.query.get(gid)
        req_json = request.json
        genre.name = req_json.get('name')
        db.session.add(genre)
        db.session.commit()
        return ""
    
    def delete_genre(self, gid):
        genre = Genre.query.get(gid)
        db.session.delete(genre)
        db.session.commit()
        return ""