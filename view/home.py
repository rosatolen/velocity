import web
import forms
from model.task import SnailTask, QuailTask
from model.prize_area import PrizeArea
from model.todo_list import TodoList
from model.repositories.reward_repository import RewardRepository
from model.repositories.task_repository import TaskRepository
from model.repositories.bad_ass_points_repository import BadAssPointsRepository
from model.bad_ass_points_purse import BadAssPointsPurse
from model.repositories.mongo_wrapper import MongoWrapper


class Home:
    def __init__(self):
        self.prize_area = PrizeArea(RewardRepository(MongoWrapper()),
                                    BadAssPointsPurse(BadAssPointsRepository(MongoWrapper())))
        self.todo_list = TodoList(TaskRepository(MongoWrapper()),
                                  BadAssPointsPurse(BadAssPointsRepository(MongoWrapper())))
        self.bad_ass_points_purse = BadAssPointsPurse(BadAssPointsRepository(MongoWrapper()))
        self.snail_task_form = forms.SnailTaskForm().form
        self.quail_task_form = forms.QuailTaskForm().form
        self.watermelon_task_form = forms.WatermelonTaskForm().form
        self.reward_form = forms.RewardForm().form
        self.complete_task_form = forms.CompleteTaskForm().form
        self.purchase_reward_form = forms.PurchaseRewardForm().form
        self.render = web.template.render('templates',
                                          globals={'is_snail': is_snail,
                                                   'is_quail': is_quail})

    def render_home_page(self, error=None):
        bad_ass_points_total = self.bad_ass_points_purse.total
        rewards = self.prize_area.get_rewards()
        tasks = self.todo_list.get_tasks()

        return self.render.home(error,
                                bad_ass_points_total,
                                rewards,
                                tasks,
                                self.reward_form,
                                self.snail_task_form,
                                self.quail_task_form,
                                self.watermelon_task_form,
                                self.complete_task_form,
                                self.purchase_reward_form)

    def GET(self):
        return self.render_home_page()


def is_snail(task):
    return isinstance(task, SnailTask)


def is_quail(task):
    return isinstance(task, QuailTask)
