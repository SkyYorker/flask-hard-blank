
from container import auth_service
from flask_restx import Resource, Namespace
from flask import request

auth_ns = Namespace('auth')


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