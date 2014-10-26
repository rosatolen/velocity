from pymongo import MongoClient
from model.task import *


class TaskRepository:
    def __init__(self, mongo_repository):
        self.tasks = mongo_repository

    def get_tasks(self):
        tasks = []
        for task in self.tasks.find_tasks():
            if task['size'] == 'snail':
                print 'database poped a snail'
                tasks.append(SnailTask(task['name']))
            else:
                print 'database poped a quail'
                tasks.append(QuailTask(task['name']))
        return tasks

    def add(self, task):
        if task.is_snail:
            new_task = {"name": task.name, "size": "snail"}
        else:
            print 'database inserted a quail'
            new_task = {"name": task.name, "size": "quail"}
        self.tasks.insert_task(new_task)
