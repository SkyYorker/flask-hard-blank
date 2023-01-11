import base64
import hashlib
import hmac
from constants import PWD_HASH_SALT, PWD_HASH_ITERATIONS
from dao.users import UserDAO


class UserService:
    def __init__(self, user_dao: UserDAO):
        self.user_dao = user_dao

    def get_hash(self, password):
        return base64.b64encode(hashlib.pbkdf2_hmac(
            'sha256',
            password.encode('utf-8'),
            PWD_HASH_SALT,
            PWD_HASH_ITERATIONS
        ))

    def compare_password(self, password_hash, password):
        string_hash_1 = password_hash
        string_hash_2 = self.get_hash(password)
        print(string_hash_1, string_hash_2)
        
        return hmac.compare_digest(
            base64.b64decode(password_hash),
            base64.b64decode(self.get_hash(password)))
        

    def get_by_username(self,username):
        return self.user_dao.get_by_username(username)

    def get_all_users(self):
        return self.user_dao.get_all_users()

    def get_user_by_id(self,uid):
        return self.user_dao.get_user_by_id(uid)

    def add_user(self, user):
        user["password"] = self.get_hash(user["password"])
        return self.user_dao.add_user()

    def put_user(self):
        return self.user_dao.put_user()

    def delete_user(self):
        return self.user_dao.delete_user()