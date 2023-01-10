
from flask_restx import Resource, Namespace
from flask import request
from container import user_service
from container import auth_service

user_ns = Namespace('users')
auth_ns = Namespace('auth')

@user_ns.route('/')
class UsersView(Resource):
    def get(self):
        return user_service.get_all_users(), 201

    def post(self):
        req_json = request.json
        user = user_service.add_user(req_json)
        return "Пользователь добавлен", 201, {"location": f"/users/{user.id}"}


@user_ns.route('/<int:uid>')
class UserView(Resource):
    def get(self,uid):
        return user_service.get_user_by_id(uid), 201

    def put(self,uid):
        return user_service.put_user(uid)

@user_ns.route('/<username>')
class UserView(Resource):
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

        tokens = auth_service.generate_token(ref_token)
        if tokens:
            return tokens
        else:
            return "", 400