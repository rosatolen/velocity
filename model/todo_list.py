from model.task import SnailTask
from model.task import QuailTask


class TodoList:
    def __init__(self, task_repository, bad_ass_points_purse):
        self.bad_ass_points_purse = bad_ass_points_purse
        self.task_repository = task_repository

    def complete(self, name):
        task = self.task_repository.get_task(name)
        self.bad_ass_points_purse.add_bad_ass_points_for(task)
        self.task_repository.delete_task(name)

    def add(self, task):
        self.task_repository.add(task)

    def contains(self, task):
        return self.task_repository.contains(task)

    def get_tasks(self):
        return self.task_repository.get_tasks()
