import calendar
import datetime
from constants import JWT_ALGO, JWT_SECRET
from service.users import UserService
import jwt

class AuthService:
    def __init__(self, user_service: UserService):
        self.user_service = user_service

    def  generate_token(self, username, password, is_refresh=False):
        user = self.user_service.get_by_username(username)

        if not user:
            raise Exception("Не найден пользователь")

        if not is_refresh:
            if not self.user_service.compare_password(user["password"], password):
                raise Exception('Не верный пароль')


        data = {
            'username': user["username"],
            'role': user["role"]
            
        }

        min30 = datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
        data['exp'] = calendar.timegm(min30.timetuple())
        access_token = jwt.encode(data, JWT_SECRET, algorithm=JWT_ALGO)

        day30 = datetime.datetime.utcnow() + datetime.timedelta(days=30)
        data['exp'] = calendar.timegm(day30.timetuple())
        refresh_token = jwt.encode(data, JWT_SECRET, algorithm=JWT_ALGO)
        
        return {"access_token":access_token, "refresh_token":refresh_token}

    def approve_refresh_token(self, refresh_token):
        data = jwt.decode(refresh_token, JWT_SECRET, algorithms=[JWT_ALGO])
        username = data['username']
        user = self.user_service.get_by_username(username)

        if not user:
            raise Exception("плохой токен")

        return self.generate_token(username, user.password,is_refresh=True)