import web
import forms
from home import Home
from model.repositories.reward_repository import RewardRepository
from model.repositories.task_repository import TaskRepository
from model.repositories.bad_ass_points_repository import BadAssPointsRepository
from model.repositories.mongo_wrapper import MongoWrapper
from model.bad_ass_points_purse import BadAssPointsPurse
from model.todo_list import TodoList


class CompleteTask:
    def __init__(self):
        self.todo_list = TodoList(TaskRepository(MongoWrapper()), BadAssPointsPurse(BadAssPointsRepository(MongoWrapper())))
        self.home = Home()

    def POST(self, name):
        complete_task_form = self.home.complete_task_form
        if not complete_task_form.validates():
            return self.home.render_home_page()

        self.todo_list.complete(name)
        raise web.seeother('/')
