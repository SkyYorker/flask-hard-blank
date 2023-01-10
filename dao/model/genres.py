
from setup_db import db
from marshmallow import Schema, fields

class Genre(db.Model):
    __tablename__ = 'genre'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    
    
class GenresSchema(Schema):
    id = fields.Int()
    name = fields.Str()
    

genre_schema = GenresSchema()
genres_schema = GenresSchema(many=True)