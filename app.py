import web
import view
from model.task import SnailTask
from model.user import User
from model.user_factory import UserFactory, InvalidCredentials
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
    return web.session.Session(app, web.session.DiskStore('sessions'), initializer={'user': None})


class Login:
    def __init__(self):
        self.login_form = web.form.Form(
            web.form.Textbox('username', web.form.notnull, description="Username"),
            web.form.Password('password', web.form.notnull, description="Password"),
            web.form.Button('login', html='Login')
        )

    def render_login_page(self, error=None):
        return web.template.render('templates', globals()).login(error, self.login_form)

    def GET(self):
        return self.render_login_page()

    def POST(self):
        if not self.login_form.validates():
            return self.render_login_page()

        username = self.login_form.d.username
        password = self.login_form.d.password

        try:
            user_factory = UserFactory(UserRepository(MongoWrapper()))
            user_factory.create_user(username, password)

            web.config.session = create_session()
            raise web.seeother('/')
        except InvalidCredentials:
            error = "Invalid Username or Password"
            return self.render_login_page(error)


class Logout:
    def __init__(self):
        pass

    def GET(self):
        web.config.session = None
        raise web.seeother('/login')


if __name__ == "__main__":
    main()
