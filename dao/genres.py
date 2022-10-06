from .model.genres import Genre, genres_schema, genre_schema

class GenreDAO:
    def get_all_genres(self):
        all_genres = Genre.query.all()
        return genres_schema.dump(all_genres)
    
    def get_genre_by_id(self, gid):
        genre = Genre.query.get(gid)
        return genre_schema.dump(genre)