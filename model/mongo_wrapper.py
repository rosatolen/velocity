from pymongo import MongoClient


class MongoWrapper:
    def __init__(self):
        self.tasks = MongoClient('mongodb://localhost:27017').velocity.tasks
        self.rewards = MongoClient('mongodb://localhost:27017').velocity.rewards

    def insert_reward(self, reward):
        self.rewards.insert(reward)

    def find_rewards(self):
        return self.rewards.find()

    def insert_task(self, task):
        self.tasks.insert(task)

    def find_tasks(self):
        return self.tasks.find()
