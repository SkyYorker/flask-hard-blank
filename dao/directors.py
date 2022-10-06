from .model.directors import Director, director_schema, directors_schema


class DirectorDAO:
    def get_all_directors(self):
        all_directors = Director.query.all()
        return directors_schema.dump(all_directors)
    
    def get_director_by_id(self, did):
        director = Director.query.get(did)
        return director_schema.dump(director)