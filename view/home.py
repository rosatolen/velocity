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
        self.snail_task_form = forms.SnailTaskForm().form
        self.reward_form = forms.RewardForm().form
        self.quail_task_form = forms.QuailTaskForm().form
        self.complete_task_form = forms.CompleteTaskForm().form

    def render_home_page(self):
        bad_ass_points_total = self.bad_ass_points_purse.total
        rewards = self.reward_repository.get_rewards()
        tasks = self.task_repository.get_tasks()

        return self.render.home(bad_ass_points_total,
                                rewards,
                                self.reward_form,
                                tasks,
                                self.snail_task_form,
                                self.quail_task_form,
                                self.complete_task_form)

    def GET(self):
        return self.render_home_page()
