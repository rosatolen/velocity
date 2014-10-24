import web
from reward_repository import RewardRepository
from reward import Reward

class Home:
  form = web.form.Form(
    web.form.Textbox('new_reward_name',  web.form.notnull, description=""),
    web.form.Textbox('new_reward_cost', web.form.notnull, description=""),
    web.form.Button('Add Reward'),
  )
  reward_repository = RewardRepository()
  render = web.template.render('templates')

  def GET(self):
    rewards = self.reward_repository.get_rewards()
    form = self.form()
    return self.render.home(rewards, form)

  def POST(self):
    form = self.form()
    if not form.validates():
      return self.render.home(form)

    new_reward = Reward(form.d.new_reward_name, form.d.new_reward_cost)
    self.reward_repository.add(new_reward)
    raise web.seeother('/')
