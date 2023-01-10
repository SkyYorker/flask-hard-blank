from dao.genres import GenreDAO


class GenreService:
    def __init__(self, genre_dao: GenreDAO):
       self.genre_dao = genre_dao
       
    def get_all_genres(self):
        return self.genre_dao.get_all_genres()
    
    def get_genre_by_id(self, gid):
        return self.genre_dao.get_genre_by_id(gid)

    def add_genre(self):
        return self.genre_dao.add_genre()

    def put_genre(self):
        return self.genre_dao.put_genre()

    def delete_genre(self):
        return self.genre_dao.delete_genre()