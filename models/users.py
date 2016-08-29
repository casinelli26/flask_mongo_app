import uuid
from common.database import Database

class User(object):
    def __init__(self, username, password, _id=None):
        self.username = username
        self.password = password
        self._id = uuid.uuid4().hex if _id is None else _id

    def save_to_database(self):
        Database.insert(collection='user_data', data=self.json())

    @classmethod
    def find_username(cls, username):
        user = Database.find_one(collection='user_data', query={"username": username})
        return user

    def json(self):
        return {
            "_id": self._id,
            "username": self.username,
            "password": self.password,
        }
