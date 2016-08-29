from passlib.hash import pbkdf2_sha512
import re

class Util(object):

    @staticmethod
    def username_is_valid(username):
        username_matcher = re.compile('/^[a-z0-9_-]{3,16}$/')
        return True if username_matcher.match(username) else False

    @staticmethod
    def hash_password(password):
        return pbkdf2_sha512.encrypt(password)

    @staticmethod
    def check_hashed_password(password, hashed_password):
        return pbkdf2_sha512.verify(password, hashed_password)