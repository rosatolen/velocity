import os
from pymongo import MongoClient


class MongoWrapper:
    def __init__(self):
        try:
            mongolab_uri = os.environ['MONGOLAB_URI']
            db = MongoClient(mongolab_uri)
            self.users = db.get_default_database().users
        except KeyError:
            client = MongoClient('mongodb://localhost:27017')
            self.users = client.velocity.users

    def get_salt(self, username):
        user = self.users.find_one({'username': username})
        return user['salt']

    def get_password(self, username):
        user = self.users.find_one({'username': username})
        return user['password']

    def insert(self, query):
        self.users.insert(query)

    def remove(self, query):
        self.users.remove(query)

    def find_one(self, query):
        return self.users.find_one(query)
