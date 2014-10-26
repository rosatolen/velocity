import web
import forms
from model.reward import Reward
from model.reward_repository import RewardRepository
from model.task import *
from model.task_repository import TaskRepository


class CreateReward:
    def __init__(self):
        self.reward_repository = RewardRepository()
        self.task_repository = TaskRepository()
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
        self.task_repository = TaskRepository()
        self.reward_repository = RewardRepository()
        self.render = web.template.render('templates')

    def POST(self):
        reward_form = forms.RewardForm().form
        snail_task_form = forms.SnailTaskForm().form
        quail_task_form = forms.QuailTaskForm().form
        rewards = self.reward_repository.get_rewards()
        tasks = self.task_repository.get_tasks()
        if not snail_task_form.validates():
            return self.render.home(rewards, reward_form, tasks, snail_task_form, quail_task_form)

        new_task = SnailTask(snail_task_form.d.new_snail_task_name)
        self.task_repository.add(new_task)
        raise web.seeother('/')


class CreateQuailTask:
    def __init__(self):
        self.task_repository = TaskRepository()
        self.reward_repository = RewardRepository()
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
