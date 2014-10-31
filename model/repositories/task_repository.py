from pymongo import MongoClient
from model.task import *


class TaskRepository:
    def __init__(self, mongo_repository):
        self.tasks = mongo_repository

    def add(self, task):
        if isinstance(task, SnailTask):
            new_task = {"name": task.name, "size": "snail"}
        elif isinstance(task, QuailTask):
            new_task = {"name": task.name, "size": "quail"}
        else:
            new_task = {"name": task.name, 'size': 'watermelon'}
        self.tasks.insert_task(new_task)

    def get_tasks(self):
        tasks = []
        for task in self.tasks.find_tasks():
            tasks.append(create_task(task))
        return tasks

    def get_task(self, name):
        for task in self.tasks.find_tasks():
            if task['name'] == name:
                return create_task(task)

    def delete_task(self, name):
        self.tasks.remove({'name': name})

    def contains(self, task_name):
        for task in self.tasks.find_tasks():
            if task['name'] == task_name:
                return True
        return False


def create_task(db_task):
    if db_task['size'] == 'snail':
        return SnailTask(db_task['name'])
    elif db_task['size'] == 'quail':
        return QuailTask(db_task['name'])
    else:
        return WatermelonTask(db_task['name'])
