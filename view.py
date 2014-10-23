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
    web.form.Textbox('Name',  web.form.notnull),
    web.form.Textbox('Cost', web.form.notnull),
    web.form.Button('Add Reward'),
  )

  def GET(self):
    reward_repository = RewardRepository()
    rewards = reward_repository.get_rewards()
    form = self.form()
    return render.home(rewards, form)

  def POST(self):
    form = self.form()
    if not form.validates():
      return render.home(form)

    reward = Reward(form.d.Name, form.d.Cost)
    reward_repository = RewardRepository()
    reward_repository.add(reward)
    raise web.seeother('/')

if __name__ == "__main__":
  main()
