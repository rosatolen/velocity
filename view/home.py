import web
import forms
from model.reward_repository import RewardRepository
from model.task_repository import TaskRepository


class Home:
    def __init__(self):
        self.reward_repository = RewardRepository()
        self.task_repository = TaskRepository()
        self.render = web.template.render('templates')

    def GET(self):
        rewards = self.reward_repository.get_rewards()
        tasks = self.task_repository.get_tasks()
        reward_form = forms.RewardForm().form
        snail_task_form = forms.SnailTaskForm().form
        quail_task_form = forms.QuailTaskForm().form
        return self.render.home(rewards, reward_form, tasks, snail_task_form, quail_task_form)
