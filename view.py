import web
from web.contrib.template import render_jinja
from reward_repository import *
from reward import *

def main():
  urls = (
    '/', 'Home'
  )
  app = web.application(urls, globals())
  app.run()

render = web.template.render('templates')

class Home:
  form = web.form.Form(
    web.form.Textbox('new_reward_name',  web.form.notnull, description=""),
    web.form.Textbox('new_reward_cost', web.form.notnull, description=""),
    web.form.Button('Add Reward'),
  )
  reward_repository = RewardRepository()

  def GET(self):
    rewards = self.reward_repository.get_rewards()
    form = self.form()
    return render.home(rewards, form)

  def POST(self):
    form = self.form()
    if not form.validates():
      return render.home(form)

    new_reward = Reward(form.d.new_reward_name, form.d.new_reward_cost)
    self.reward_repository.add(new_reward)
    raise web.seeother('/')

if __name__ == "__main__":
  main()
