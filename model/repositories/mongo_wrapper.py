from pymongo import MongoClient


class MongoWrapper:
    def __init__(self):
        self.tasks = MongoClient('mongodb://localhost:27017').velocity.tasks
        self.rewards = MongoClient('mongodb://localhost:27017').velocity.rewards
        self.rapport = MongoClient('mongodb://localhost:27017').velocity.rapport

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

    def get_total(self):
        total = self.rapport.distinct('total')
        if not total:
            return None
        else:
            return total.pop()

    def increment_rapport_by(self, number):
        i = self.rapport.distinct('total').pop()
        self.rapport.find_and_modify({'total': i}, {'$inc': {'total': number}})

    def initialize_rapport(self, initial_value):
        self.rapport.insert(initial_value)
