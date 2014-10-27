import web
import forms
from model.repositories.reward_repository import RewardRepository
from model.repositories.task_repository import TaskRepository
from model.rapport_purse import RapportPurse
from model.repositories.mongo_wrapper import MongoWrapper


class Home:
    def __init__(self):
        self.reward_repository = RewardRepository(MongoWrapper())
        self.task_repository = TaskRepository(MongoWrapper())
        self.rapport_purse = RapportPurse(MongoWrapper())
        self.render = web.template.render('templates')

    def GET(self):
        rapport_total = self.rapport_purse.total
        rewards = self.reward_repository.get_rewards()
        tasks = self.task_repository.get_tasks()
        reward_form = forms.RewardForm().form
        snail_task_form = forms.SnailTaskForm().form
        quail_task_form = forms.QuailTaskForm().form
        complete_task_form = forms.CompleteTaskForm().form
        return self.render.home(rapport_total, rewards, reward_form, tasks, snail_task_form, quail_task_form, complete_task_form)
