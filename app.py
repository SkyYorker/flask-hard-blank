
from flask import Flask
from flask_restx import Api

from setup_db import db
from config import Config
from views.movies import movies_ns
from views.directors import directors_ns
from views.genres import genres_ns
from views.users import user_ns
from views.auth import auth_ns

def create_app(config_object):
    app = Flask(__name__)
    app.config.from_object(config_object)
    db.init_app(app)
    with app.app_context(): 
        db.create_all()
    register_extensions(app)
    return app

def register_extensions(app):
    db.init_app(app)
    api = Api(app)
    api.add_namespace(movies_ns)
    api.add_namespace(directors_ns)
    api.add_namespace(genres_ns)
    api.add_namespace(user_ns)
    api.add_namespace(auth_ns)


app = create_app(Config)

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=9999)