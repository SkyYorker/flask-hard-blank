

from dao.movies import MovieDAO
from dao.directors import DirectorDAO
from dao.genres import GenreDAO
from dao.users import UserDAO

from service.movies import MovieService
from service.directors import DirectorsService
from service.genres import GenreService
from service.users import UserService
from service.auth import AuthService

movie_dao = MovieDAO()
movie_service = MovieService(movie_dao)

director_dao = DirectorDAO()
director_service = DirectorsService(director_dao)

genre_dao = GenreDAO()
genre_service = GenreService(genre_dao)

user_dao = UserDAO()
user_service = UserService(user_dao)

# auth_dao = AuthService()
auth_service = AuthService(user_service)