import sys
from pymongo import MongoClient
from task import *

class TaskRepository:
  def __init__(self):
    self.tasks = MongoClient('mongodb://localhost:27017').velocity.tasks

  def add(self, task):
    new_task = { "name" : task.name }
    self.tasks.insert(new_task)

  def get_tasks(self):
    tasks = []
    for task in self.tasks.find():
      tasks.append(SnailTask(task['name']))
    return tasks
