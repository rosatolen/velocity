import web
from web.form import Validator
from model.user_repository import UserRepository, MongoWrapper, UserFactory


class RewardForm:
    def __init__(self):
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
        user_factory = UserFactory(UserRepository(MongoWrapper()))
        user = user_factory.find_user(web.cookies().get('username'))
        return not user.has_reward_named(value)


class SnailTaskForm:
    def __init__(self):
        self.form = web.form.Form(
            web.form.Textbox('new_snail_task_name', web.form.notnull,
                             Validator("Task already exists", self.not_existing_task),
                             description=""),
            web.form.Button('submit_snail_task', html='Add Snail Task'),
        )

    def not_existing_task(self, value):
        user_factory = UserFactory(UserRepository(MongoWrapper()))
        user = user_factory.find_user(web.cookies().get('username'))
        return not user.has_task_named(value)


class QuailTaskForm:
    def __init__(self):
        self.form = web.form.Form(
            web.form.Textbox('new_quail_task_name', web.form.notnull,
                             Validator("Task already exists", self.not_existing_task),
                             description=""),
            web.form.Button('submit_quail_task', html='Add Quail Task'),
        )

    def not_existing_task(self, value):
        user_factory = UserFactory(UserRepository(MongoWrapper()))
        user = user_factory.find_user(web.cookies().get('username'))
        return not user.has_task_named(value)


class WatermelonTaskForm:
    def __init__(self):
        self.form = web.form.Form(
            web.form.Textbox('new_watermelon_task_name', web.form.notnull,
                             Validator("Task already exists", self.not_existing_task),
                             description=""),
            web.form.Button('submit_watermelon_task', html='Add Watermelon Task'),
        )

    def not_existing_task(self, value):
        user_factory = UserFactory(UserRepository(MongoWrapper()))
        user = user_factory.find_user(web.cookies().get('username'))
        return not user.has_task_named(value)


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
