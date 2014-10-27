from model.task import SnailTask


class TodoList:
    def __init__(self, task_repository, rapport_purse):
        self.rapport_purse = rapport_purse
        self.mongo_task_repository = task_repository

    def complete(self, name):
        self.mongo_task_repository.delete_task({'name': name})
        self.rapport_purse.add_rapport_for(SnailTask(name))
