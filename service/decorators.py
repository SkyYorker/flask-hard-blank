from flask import request, abort
import jwt
from constants import JWT_SECRET, JWT_ALGO

def auth_requered(func):
    def wrapper(*args, **kwargs):
        if not "Authorization" in request.headers:
            abort(401)
            
        token = request.headers["Authorization"]
        try:
            jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGO])
        except Exception as e:
            print(f"JWT decode error: {e}")
            abort(403)
            
        return func(*args, **kwargs)
    
    return wrapper


def admin_requred(func):
    def wrapper(*args, **kwargs):
        if not "Authorization" in request.headers:
            abort(401)
            
        token = request.headers["Authorization"]
        try:
            data = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGO])
        except Exception as e:
            print(f"JWT decode error: {e}")
            abort(403)
        else:
            if data["role"] == "admin":                
                return func(*args, **kwargs)
            
            if data["role"] != "admin":
                abort(403)
            
        abort(401)
    
    return wrapper