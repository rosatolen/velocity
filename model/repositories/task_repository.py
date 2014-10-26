from pymongo import MongoClient
from model.task import *


class TaskRepository:
    def __init__(self, mongo_repository):
        self.tasks = mongo_repository

    def add(self, task):
        if task.is_snail():
            new_task = {"name": task.name, "size": "snail"}
        else:
            new_task = {"name": task.name, "size": "quail"}
        self.tasks.insert_task(new_task)

    def get_tasks(self):
        tasks = []
        for task in self.tasks.find_tasks():
            if task['size'] == 'snail':
                tasks.append(SnailTask(task['name']))
            else:
                tasks.append(QuailTask(task['name']))
        return tasks
