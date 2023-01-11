
from flask_restx import Resource, Namespace
from flask import request
from container import user_service
from container import auth_service
from service.decorators import admin_requred, auth_requered


user_ns = Namespace('users')
auth_ns = Namespace('auth')

@user_ns.route('/')
class UsersView(Resource):
    
    @auth_requered
    def get(self):
        return user_service.get_all_users(), 201

    @admin_requred
    def post(self):
        req_json = request.json
        user = user_service.add_user(req_json)
        return "Пользователь добавлен", 201, {"location": f"/users/{user.id}"}


@user_ns.route('/<int:uid>')
class UserView(Resource):
    
    @auth_requered
    def get(self,uid):
        return user_service.get_user_by_id(uid), 201

    @admin_requred
    def put(self,uid):
        return user_service.put_user(uid)
    
    @admin_requred
    def delete(self,uid):
        return user_service.delete_user(uid)
    
    
@user_ns.route('/<username>')
class UserView(Resource):
    
    @auth_requered
    def get(self,username):
        return user_service.get_by_username(username), 201

    

@auth_ns.route('/')
class AuthView(Resource):
    def post(self):
        req_json = request.json
        username = req_json.get("username")
        password = req_json.get("password")
        if not (username or password):
            return "Нужно имя и пароль", 400

        tokens = auth_service.generate_token(username, password)
        if tokens:
            return tokens
        else:
            return "", 400

    
    def put(self):
        req_json = request.json
        ref_token = req_json.get("refresh_token")
        username = req_json.get('username')

        tokens = auth_service.generate_token(username, ref_token)
        if tokens:
            return tokens
        else:
            return "", 400