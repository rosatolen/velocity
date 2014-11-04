import web
import forms
from app import app
from model.task import SnailTask, QuailTask
from model.repositories.mongo_wrapper import MongoWrapper
from model.repositories.user_repository import UserRepository
from model.user_factory import UserFactory


class Home:
    def __init__(self):
        self.snail_task_form = forms.SnailTaskForm().form
        self.quail_task_form = forms.QuailTaskForm().form
        self.watermelon_task_form = forms.WatermelonTaskForm().form
        self.reward_form = forms.RewardForm().form
        self.complete_task_form = forms.CompleteTaskForm().form
        self.purchase_reward_form = forms.PurchaseRewardForm().form
        self.render = web.template.render('templates',
                                          globals={'is_snail': is_snail,
                                                   'is_quail': is_quail})

    def render_home_page(self, user, error=None):
        return self.render.home(error,
                                user.points,
                                user.rewards,
                                user.tasks,
                                self.reward_form,
                                self.snail_task_form,
                                self.quail_task_form,
                                self.watermelon_task_form,
                                self.complete_task_form,
                                self.purchase_reward_form)

    def GET(self):
        if web.config.get('session') is None:
            raise web.seeother('/login')
        else:
            #session_user = web.config.get('session')._initializer['user']
            #user_factory = UserFactory(UserRepository(MongoWrapper()))
            #user = user_factory.get_user(session_user.username)
            user = web.config.get('session')._initializer['user']
            return self.render_home_page(user)


def is_snail(task):
    return isinstance(task, SnailTask)


def is_quail(task):
    return isinstance(task, QuailTask)
