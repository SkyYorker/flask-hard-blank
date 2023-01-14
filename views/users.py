
from flask_restx import Resource, Namespace
from flask import request
from container import user_service

from service.decorators import admin_requred, auth_requered


user_ns = Namespace('users')


@user_ns.route('/')
class UsersView(Resource):
    
    @auth_requered
    def get(self):
        return user_service.get_all_users(), 201

    
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

    

