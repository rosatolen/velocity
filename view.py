import web
import view
from model.task import SnailTask
from model.user import User
from model.repositories.user_repository import UserRepository
from model.repositories.mongo_wrapper import MongoWrapper

urls = (
    '/', 'view.Home',
    '/login', 'Login',
    '/logout', 'Logout',
    '/register', 'view.Register',
    '/create/reward', 'view.CreateReward',
    '/create/task/snail', 'view.CreateSnailTask',
    '/create/task/quail', 'view.CreateQuailTask',
    '/create/task/watermelon', 'view.CreateWatermelonTask',
    '/complete/task/(.+)', 'view.CompleteTask',
    '/purchase/(.+)', 'view.PurchaseReward',
)
app = web.application(urls, globals())


def main():
    app.run()


def create_session():
    return web.session.Session(app, web.session.DiskStore('sessions'))


def kill_session():
    web.config.session.kill()


class Login:
    def __init__(self):
        self.login_form = web.form.Form(
            web.form.Textbox('username', description="Username"),
            web.form.Textbox('password', description="Password"),
            web.form.Button('login', html='Login')
        )

    def GET(self):
        return web.template.render('templates', globals()).login(self.login_form)

    def POST(self):
        if not self.login_form.validates():
            return web.template.render('templates', globals()).login(self.login_form)

        username = self.login_form.d.username
        password = self.login_form.d.password
        user = User(username, password, UserRepository(MongoWrapper()))

        web.config.session = create_session()
        raise web.seeother('/')


class Logout:
    def __init__(self):
        pass

    def GET(self):
        kill_session()
        raise web.seeother('/login')


if __name__ == "__main__":
    main()
