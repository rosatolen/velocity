import os
from pymongo import MongoClient


class MongoWrapper:
    def __init__(self):
        try:
            mongolab_uri = os.environ['MONGOLAB_URI']
            client = MongoClient(mongolab_uri)
        except KeyError:
            client = MongoClient('mongodb://localhost:27017')

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
