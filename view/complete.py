import web
import forms
from model.repositories.reward_repository import RewardRepository
from model.repositories.task_repository import TaskRepository
from model.repositories.mongo_wrapper import MongoWrapper
from model.rapport_purse import RapportPurse
from model.todo_list import TodoList


class CompleteTask:
    def __init__(self):
        self.reward_repository = RewardRepository(MongoWrapper())
        self.task_repository = TaskRepository(MongoWrapper())
        self.render = web.template.render('templates')

    def POST(self, name):
        reward_form = forms.RewardForm().form
        snail_task_form = forms.SnailTaskForm().form
        quail_task_form = forms.QuailTaskForm().form
        complete_task_form = forms.CompleteTaskForm().form
        rewards = self.reward_repository.get_rewards()
        tasks = self.task_repository.get_tasks()

        if not complete_task_form.validates():
            return self.render.home(rewards, reward_form, tasks, snail_task_form, quail_task_form, complete_task_form)

        todo_list = TodoList(TaskRepository(MongoWrapper()), RapportPurse(MongoWrapper()))
        todo_list.complete(name)
        raise web.seeother('/')
