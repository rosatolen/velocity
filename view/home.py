import web
import forms
from model.repositories.reward_repository import RewardRepository
from model.repositories.task_repository import TaskRepository
from model.repositories.bad_ass_points_repository import BadAssPointsRepository
from model.bad_ass_points_purse import BadAssPointsPurse
from model.repositories.mongo_wrapper import MongoWrapper


class Home:
    def __init__(self):
        self.reward_repository = RewardRepository(MongoWrapper())
        self.task_repository = TaskRepository(MongoWrapper())
        self.bad_ass_points_purse = BadAssPointsPurse(BadAssPointsRepository(MongoWrapper()))
        self.render = web.template.render('templates')

    def GET(self):
        bad_ass_points_total = self.bad_ass_points_purse.total
        rewards = self.reward_repository.get_rewards()
        tasks = self.task_repository.get_tasks()

        reward_form = forms.RewardForm().form
        snail_task_form = forms.SnailTaskForm().form
        quail_task_form = forms.QuailTaskForm().form
        complete_task_form = forms.CompleteTaskForm().form

        return self.render.home(bad_ass_points_total, rewards, reward_form, tasks, snail_task_form, quail_task_form,
                                complete_task_form)
