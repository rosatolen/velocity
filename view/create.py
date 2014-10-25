import web
from reward import Reward
from reward_repository import RewardRepository

class CreateReward:
  form = web.form.Form(
    web.form.Textbox('new_reward_name', web.form.notnull, description=""),
    web.form.Textbox('new_reward_cost', web.form.notnull, description=""),
    web.form.Button('Add Reward'),
  )
  reward_repository = RewardRepository()
  render = web.template.render('templates')

  def POST(self):
    form = self.form()
    if not form.validates():
      return self.render.home(form)

    new_reward = Reward(form.d.new_reward_name, form.d.new_reward_cost)
    self.reward_repository.add(new_reward)
    raise web.seeother('/')
