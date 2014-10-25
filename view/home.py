import web
import forms
from reward_repository import RewardRepository
from reward import Reward

class Home:
  def __init__(self):
    self.reward_repository = RewardRepository()
    self.render = web.template.render('templates')

  def GET(self):
    rewards = self.reward_repository.get_rewards()
    form = forms.RewardForm().form
    return self.render.home(rewards, form)
