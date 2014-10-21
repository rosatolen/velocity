import web
from web.contrib.template import render_jinja

urls = (
'/(.*)', 'Home'
)
render = render_jinja('templates', encoding='utf-8',)
app = web.application(urls, globals())

class Home:
  def GET(self, name):
    return render.hello(name=name)

if __name__ == "__main__":
  app.run()
