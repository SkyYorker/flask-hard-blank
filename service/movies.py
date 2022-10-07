
from dao.movies import MovieDAO

from flask import request


class MovieService:
    def __init__(self, movie_dao: MovieDAO):
        self.movie_dao = movie_dao
        
    def add_movie(self):
        return self.movie_dao.add_movie()
        
    def get_movie_by_id(self, mid):
        return self.movie_dao.get_movie_by_id(mid)   
        
    def all_movies(self):
        return self.movie_dao.get_all_movie()
    
    def put_movie(self, mid):
        return self.movie_dao.put_movie(mid)
    
    def get_movies_by_fields(self):
        if 'director_id' in request.args:
            return MovieDAO.get_movies_by_director(self)
        if 'genre_id' in request.args:
            return MovieDAO.get_movies_by_genre(self)
        if 'year' in request.args:
            return MovieDAO.get_movies_by_year(self)
        return MovieDAO.get_all_movie(self)
    
    def delete_movie(self, mid):
        return self.movie_dao.delete_movie(mid)

