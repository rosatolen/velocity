import web
import forms
from reward_repository import RewardRepository
from reward import Reward
from task_repository import TaskRepository

class Home:
  def __init__(self):
    self.reward_repository = RewardRepository()
    self.task_repository = TaskRepository()
    self.render = web.template.render('templates')

  def GET(self):
    rewards = self.reward_repository.get_rewards()
    tasks = self.task_repository.get_tasks()
    reward_form = forms.RewardForm().form
    task_form = forms.TaskForm().form
    return self.render.home(rewards, reward_form, tasks, task_form)
