from pymongo import MongoClient

class Database(object):
    URI = 'mongodb://localhost:27017/'
    database = None

    @staticmethod
    def initialize(database):
        client = MongoClient(Database.URI)
        Database.database = client[database]

    @staticmethod
    def insert(collection, data):
        Database.database[collection].insert(data)

    @staticmethod
    def find(collection, query):
        return Database.database[collection].find(query)

    @staticmethod
    def showcollection(collection):
        return Database.database[collection].find()

    @staticmethod
    def find_one(collection, query):
        return Database.database[collection].find_one(query)

    @staticmethod
    def remove(collection, query):
        Database.database[collection].remove(query)