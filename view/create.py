import web
import forms
from reward import Reward
from reward_repository import RewardRepository
from task import SnailTask
from task_repository import TaskRepository

class CreateReward:
  def __init__(self):
    self.reward_repository = RewardRepository()
    self.task_repository = TaskRepository()
    self.render = web.template.render('templates')

  def POST(self):
    reward_form = forms.RewardForm().form
    task_form = forms.TaskForm().form
    rewards = self.reward_repository.get_rewards()
    tasks = self.task_repository.get_tasks()
    if not reward_form.validates():
      return self.render.home(rewards, reward_form, tasks, task_form)

    new_reward = Reward(reward_form.d.new_reward_name, reward_form.d.new_reward_cost)
    self.reward_repository.add(new_reward)
    raise web.seeother('/')

class CreateTask:
  def __init__(self):
    self.task_repository = TaskRepository()
    self.reward_repository = RewardRepository()
    self.render = web.template.render('templates')

  def POST(self):
    reward_form = forms.RewardForm().form
    task_form = forms.TaskForm().form
    rewards = self.reward_repository.get_rewards()
    tasks = self.task_repository.get_tasks()
    if not task_form.validates():
      return self.render.home(rewards, reward_form, tasks, task_form)

    new_task = SnailTask(task_form.d.new_snail_task_name)
    self.task_repository.add(new_task)
    raise web.seeother('/')
