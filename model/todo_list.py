class TodoList:
    def __init__(self, mongo_task_repository):
        self.mongo_task_repository = mongo_task_repository

    def complete(self, name):
        self.mongo_task_repository.delete_task({'name': name })
