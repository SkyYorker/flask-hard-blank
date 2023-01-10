from flask import request
from .model.users import User, user_shchema, users_shchema
from setup_db import db

class UserDAO():

    def get_all_users(self):
        all_users = User.query.all()
        return users_shchema.dump(all_users)
    
    def get_user_by_id(self, uid):
        movie = User.query.get(uid)
        return user_shchema.dump(movie)
        
    
    def get_by_username(self, username):
        username = User.query.filter(User.username == username).first()
        return user_shchema.dump(username)

    def add_user(self):
        req_json = request.json
        user = User(**req_json)
        db.session.add(user)
        db.session.commit()
        return user

    def put_user(self, uid):
        user = User.query.get(uid)
        req_json = request.json
        user.name = req_json.get('name')
        user.password = req_json.get('password')
        user.role = req_json.get('role')
        db.session(user)
        db.commit()
        return "Пользователь обновлён"

    def delete_user(self, uid):
        user = User.query.get(uid)
        db.session.delete(user)
        db.session.commit()
        return "Пользователь удалён"