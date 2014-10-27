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
        self.rapport = client.velocity.rapport

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

    def get(self, key):
        return self.rapport.distinct(key)

    def increment_rapport_total_by(self, number):
        i = self.rapport.distinct('total').pop()
        self.rapport.find_and_modify({'total': i}, {'$inc': {'total': number}})

    def initialize_rapport(self, initial_value):
        self.rapport.insert(initial_value)
