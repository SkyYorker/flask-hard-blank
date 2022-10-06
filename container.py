from dao import genres
from dao.movies import MovieDAO
from dao.directors import DirectorDAO
from dao.genres import GenreDAO
from setup_db import db
from service.movies import MovieService
from service.directors import DirectorsService
from service.genres import GenreService

movie_dao = MovieDAO()
movie_service = MovieService(movie_dao)

director_dao = DirectorDAO()
director_service = DirectorsService(director_dao)

genre_dao = GenreDAO()
genre_service = GenreService(genre_dao)