import os
from pymongo import MongoClient


class MongoWrapper:
    def __init__(self):
        try:
            mongolab_uri = os.environ['MONGOLAB_URI']
            db = MongoClient(mongolab_uri)
            self.users = db.get_default_database().users
            self.tasks = db.get_default_database().tasks
            self.rewards = db.get_default_database().rewards
            self.bad_ass_points = db.get_default_database().bad_ass_points
        except KeyError:
            client = MongoClient('mongodb://localhost:27017')
            self.users = client.velocity.users
            self.tasks = client.velocity.tasks
            self.rewards = client.velocity.rewards
            self.bad_ass_points = client.velocity.bad_ass_points

    def insert_reward(self, reward):
        self.rewards.insert(reward)

    def find_rewards(self):
        return self.rewards.find()

    def insert_task(self, task):
        self.tasks.insert(task)

    def find_tasks(self):
        return self.tasks.find()

    def remove(self, task):
        self.tasks.remove(task)

    def get_bad_ass_points_total(self, key):
        return self.bad_ass_points.distinct(key)

    def increment_bad_ass_points_by(self, number):
        i = self.bad_ass_points.distinct('total').pop()
        self.bad_ass_points.find_and_modify({'total': i}, {'$inc': {'total': number}})

    def initialize_bad_ass_points(self, initial_value):
        self.bad_ass_points.insert(initial_value)

    def remove_reward(self, name):
        self.rewards.remove({'name': name})

    def decrement_bad_ass_points_by(self, number):
        i = self.bad_ass_points.distinct('total').pop()
        self.bad_ass_points.update({'total': i}, {'$inc': {'total': -number}})

    def create_document(self, username, password, salt):
        self.users.insert({'username': username, 'password': password, 'salt': salt})

    def get_salt(self, username):
        user = self.users.find_one({'username': username})
        return user['salt']
