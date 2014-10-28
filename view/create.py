import web
import forms
from model.reward import Reward
from model.repositories.reward_repository import RewardRepository
from model.task import *
from model.bad_ass_points_purse import BadAssPointsPurse
from model.repositories.task_repository import TaskRepository
from model.repositories.bad_ass_points_repository import BadAssPointsRepository
from model.todo_list import TodoList
from model.repositories.mongo_wrapper import MongoWrapper


class CreateReward:
    def __init__(self):
        self.reward_repository = RewardRepository(MongoWrapper())
        self.task_repository = TaskRepository(MongoWrapper())
        self.render = web.template.render('templates')

    def POST(self):
        reward_form = forms.RewardForm().form
        snail_task_form = forms.SnailTaskForm().form
        quail_task_form = forms.QuailTaskForm().form
        rewards = self.reward_repository.get_rewards()
        tasks = self.task_repository.get_tasks()
        if not reward_form.validates():
            return self.render.home(rewards, reward_form, tasks, snail_task_form, quail_task_form)

        new_reward = Reward(reward_form.d.new_reward_name, reward_form.d.new_reward_cost)
        self.reward_repository.add(new_reward)
        raise web.seeother('/')


class CreateSnailTask:
    def __init__(self):
        self.todo_list = TodoList(TaskRepository(MongoWrapper()), BadAssPointsPurse(BadAssPointsRepository(MongoWrapper())))
        self.reward_repository = RewardRepository(MongoWrapper())
        self.render = web.template.render('templates')

    def POST(self):
        reward_form = forms.RewardForm().form
        snail_task_form = forms.SnailTaskForm().form
        quail_task_form = forms.QuailTaskForm().form
        rewards = self.reward_repository.get_rewards()
        if not snail_task_form.validates():
            return self.render.home(rewards, reward_form, tasks, snail_task_form, quail_task_form)

        new_task = SnailTask(snail_task_form.d.new_snail_task_name)
        self.todo_list.add(new_task)
        raise web.seeother('/')


class CreateQuailTask:
    def __init__(self):
        self.task_repository = TaskRepository(MongoWrapper())
        self.reward_repository = RewardRepository(MongoWrapper())
        self.render = web.template.render('templates')

    def POST(self):
        reward_form = forms.RewardForm().form
        snail_task_form = forms.SnailTaskForm().form
        quail_task_form = forms.QuailTaskForm().form
        rewards = self.reward_repository.get_rewards()
        tasks = self.task_repository.get_tasks()
        if not quail_task_form.validates():
            return self.render.home(rewards, reward_form, tasks, snail_task_form, quail_task_form)

        new_task = QuailTask(quail_task_form.d.new_quail_task_name)
        self.task_repository.add(new_task)
        raise web.seeother('/')
