import web
import forms
from reward import Reward
from reward_repository import RewardRepository

class CreateReward:
  def __init__(self):
    self.reward_repository = RewardRepository()
    self.render = web.template.render('templates')

  def POST(self):
    form = forms.RewardForm().form
    if not form.validates():
      return self.render.home(form)

    new_reward = Reward(form.d.new_reward_name, form.d.new_reward_cost)
    self.reward_repository.add(new_reward)
    raise web.seeother('/')
