import web
from home import Home
from model.reward import Reward
from model.habit import Habit
from model.task import *
from model.user_repository import UserRepository, MongoWrapper, UserFactory


class CreateReward:
    def __init__(self):
        self.home_page = Home()

    def POST(self):
        reward_form = self.home_page.reward_form
        user_factory = UserFactory(UserRepository(MongoWrapper()))
        user = user_factory.find_user(web.cookies().get('username'))

        if not reward_form.validates():
            return self.home_page.render_home_page(user)

        new_reward = Reward(reward_form.d.new_reward_name, reward_form.d.new_reward_cost)
        user.rewards.append(new_reward)

        user_repository = UserRepository(MongoWrapper())
        user_repository.save_state(user)
        raise web.seeother('/')


class CreateSnailTask:
    def __init__(self):
        self.home_page = Home()

    def POST(self):
        user_factory = UserFactory(UserRepository(MongoWrapper()))
        user = user_factory.find_user(web.cookies().get('username'))

        snail_task_form = self.home_page.snail_task_form
        if not snail_task_form.validates():
            return self.home_page.render_home_page(user)

        new_task = SnailTask(snail_task_form.d.new_snail_task_name)
        user.tasks.append(new_task)

        user_repository = UserRepository(MongoWrapper())
        user_repository.save_state(user)
        raise web.seeother('/')


class CreateQuailTask:
    def __init__(self):
        self.home_page = Home()

    def POST(self):
        user_factory = UserFactory(UserRepository(MongoWrapper()))
        user = user_factory.find_user(web.cookies().get('username'))

        quail_task_form = self.home_page.quail_task_form
        if not quail_task_form.validates():
            return self.home_page.render_home_page(user)

        new_task = QuailTask(quail_task_form.d.new_quail_task_name)
        user.tasks.append(new_task)

        user_repository = UserRepository(MongoWrapper())
        user_repository.save_state(user)
        raise web.seeother('/')


class CreateWatermelonTask:
    def __init__(self):
        self.home_page = Home()

    def POST(self):
        user_factory = UserFactory(UserRepository(MongoWrapper()))
        user = user_factory.find_user(web.cookies().get('username'))

        watermelon_task_form = self.home_page.watermelon_task_form
        if not watermelon_task_form.validates():
            return self.home_page.render_home_page(user)

        new_task = WatermelonTask(watermelon_task_form.d.new_watermelon_task_name)
        user.tasks.append(new_task)

        user_repository = UserRepository(MongoWrapper())
        user_repository.save_state(user)
        raise web.seeother('/')


class CreateHabit:
    def __init__(self):
        self.home_page = Home()

    def POST(self):
        user_factory = UserFactory(UserRepository(MongoWrapper()))
        user = user_factory.find_user(web.cookies().get('username'))

        habit_form = self.home_page.habit_form
        if not habit_form.validates():
            return self.home_page.render_home_page(user)

        habit = Habit(habit_form.d.new_habit_name)
        user.habits.append(habit)

        user_repository = UserRepository(MongoWrapper())
        user_repository.save_state(user)
        raise web.seeother('/')
