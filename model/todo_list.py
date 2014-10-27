from model.task import SnailTask
from model.task import QuailTask


class TodoList:
    def __init__(self, task_repository, rapport_purse):
        self.rapport_purse = rapport_purse
        self.task_repository = task_repository

    def complete(self, name):
        task = self.task_repository.get_task(name)
        self.rapport_purse.add_rapport_for(task)
        self.task_repository.delete_task(name)
