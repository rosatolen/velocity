import web
import forms
from home import Home
from model.repositories.user_repository import UserRepository
from model.repositories.mongo_wrapper import MongoWrapper


class CompleteTask:
    def __init__(self):
        self.home = Home()

    def POST(self, task_name):
        user = web.config.get('session').initializer['user']
        complete_task_form = self.home.complete_task_form
        if not complete_task_form.validates():
            return self.home.render_home_page(user)

        user.complete(task_name)

        user_repository = UserRepository(MongoWrapper())
        user_repository.save_state(user)
        raise web.seeother('/')
