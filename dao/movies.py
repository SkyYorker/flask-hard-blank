
from .model.movies import Movie, movie_schema, movies_schema
from flask import request
from setup_db import db


class MovieDAO:
    def get_all_movie(self):
        all_movies = Movie.query.all()
        return movies_schema.dump(all_movies)
    
    def get_movie_by_id(self, mid):
        movie = Movie.query.get(mid)
        return movie_schema.dump(movie)
        
    def get_movies_by_director(self):   
        did = request.args.get('director_id')
        all_movies = Movie.query.filter(Movie.director_id == did)
        return movies_schema.dump(all_movies)
    
    def get_movies_by_genre(self):
        gid = request.args.get('genre_id')
        all_movies = Movie.query.filter(Movie.genre_id == gid)
        return movies_schema.dump(all_movies)
    
    def get_movies_by_year(self):
        year = request.args.get('year')
        all_movies = Movie.query.filter(Movie.year == year)
        return movies_schema.dump(all_movies)
    
    def add_movie(self):
        req_json = request.json
        new_movie = Movie(**req_json)
        with db.session.begin():
            db.session.add(new_movie)
        return ""
    
    def put_movie(self, mid):
        movie = Movie.query.get(mid)
        req_json = request.json
        movie.title = req_json.get('title')
        movie.description = req_json.get('description')
        movie.trailer = req_json.get('trailer')
        movie.year = req_json.get('year')
        movie.rating = req_json.get('rating')
        movie.genre_id = req_json.get('genre_id')
        movie.director_id = req_json.get('director_id')
        db.session.add(movie)
        db.session.commit()
        return ""
    
    def delete_movie(self, mid):
        movie = Movie.query.get(mid)
        db.session.delete(movie)
        db.session.commit()
        return ""