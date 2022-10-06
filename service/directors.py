from dao.directors import DirectorDAO


class DirectorsService:
    def __init__(self, director_dao: DirectorDAO):
       self.director_dao = director_dao
       
    def get_all_directors(self):
        return self.director_dao.get_all_directors()
    
    def get_director_by_id(self, gid):
        return self.director_dao.get_director_by_id(gid)