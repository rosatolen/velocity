import web
from web.form import Validator
from model.todo_list import TodoList
from model.prize_area import PrizeArea
from model.bad_ass_points_purse import BadAssPointsPurse
from model.repositories.task_repository import TaskRepository
from model.repositories.reward_repository import RewardRepository
from model.repositories.bad_ass_points_repository import BadAssPointsRepository
from model.repositories.mongo_wrapper import MongoWrapper
from model.repositories.bad_ass_points_repository import BadAssPointsRepository


class RewardForm:
    def __init__(self):
        self.prize_area = PrizeArea(RewardRepository(MongoWrapper()),
                                    BadAssPointsPurse(BadAssPointsRepository(MongoWrapper())))
        self.form = web.form.Form(
            web.form.Textbox('new_reward_name', web.form.notnull,
                             Validator("Reward already exists", self.not_existing_reward),
                             description="New Reward Name"),
            web.form.Textbox('new_reward_cost', web.form.notnull,
                             Validator("Must be an integer", int),
                             description="New Reward Cost"),
            web.form.Button('submit_reward', html='Add Reward'),
        )

    def not_existing_reward(self, value):
        return not self.prize_area.contains(value)


class SnailTaskForm:
    def __init__(self):
        self.todo_list = TodoList(TaskRepository(MongoWrapper()),
                                  BadAssPointsPurse(BadAssPointsRepository(MongoWrapper())))
        self.form = web.form.Form(
            web.form.Textbox('new_snail_task_name', web.form.notnull,
                             Validator("Task already exists", self.not_existing_task),
                             description=""),
            web.form.Button('submit_snail_task', html='Add Snail Task'),
        )

    def not_existing_task(self, value):
        return not self.todo_list.contains(value)


class QuailTaskForm:
    def __init__(self):
        self.todo_list = TodoList(TaskRepository(MongoWrapper()),
                                  BadAssPointsPurse(BadAssPointsRepository(MongoWrapper())))
        self.form = web.form.Form(
            web.form.Textbox('new_quail_task_name', web.form.notnull,
                             Validator("Task already exists", self.not_existing_task),
                             description=""),
            web.form.Button('submit_quail_task', html='Add Quail Task'),
        )

    def not_existing_task(self, value):
        return not self.todo_list.contains(value)


class WatermelonTaskForm:
    def __init__(self):
        self.todo_list = TodoList(TaskRepository(MongoWrapper()),
                                  BadAssPointsPurse(BadAssPointsRepository(MongoWrapper())))
        self.form = web.form.Form(
            web.form.Textbox('new_watermelon_task_name', web.form.notnull,
                             Validator("Task already exists", self.not_existing_task),
                             description=""),
            web.form.Button('submit_watermelon_task', html='Add Watermelon Task'),
        )

    def not_existing_task(self, value):
        return not self.todo_list.contains(value)


class CompleteTaskForm:
    def __init__(self):
        self.form = web.form.Form(
            web.form.Button('complete', html="Complete Task")
        )


class PurchaseRewardForm:
    def __init__(self):
        self.form = web.form.Form(
            web.form.Button('purchase', html="Purchase")
        )
