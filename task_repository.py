import sys
from pymongo import MongoClient

class TaskRepository:
  def __init__(self):
    self.tasks = MongoClient('mongodb://localhost:27017').velocity.tasks

  def insert_task(self, name):
    new_task = { "Name" : name }
    self.tasks.insert(new_task)

  def view_all_tasks(self):
    for task in self.tasks.find():
      print(task)

def main(arguments):
  repository = TaskRepository()
  if 'add' in arguments[1]:
    repository.insert_task(arguments[2])
  elif 'viewall' in arguments[1]:
    repository.view_all_tasks()

if __name__ == "__main__":
  main(sys.argv)
