import web
from model.user_repository import UserRepository, MongoWrapper, UserFactory, InvalidCredentials

urls = (
    '/', 'view.Home',
    '/login', 'Login',
    '/logout', 'Logout',
    '/register', 'view.Register',

    '/create/reward', 'view.CreateReward',
    '/delete/reward/(.+)', 'view.DeleteReward',
    '/purchase/(.+)', 'view.PurchaseReward',

    '/create/habit', 'view.CreateHabit',
    '/complete/habit/(.+)', 'view.CompleteHabit',

    '/create/task/snail', 'view.CreateSnailTask',
    '/create/task/quail', 'view.CreateQuailTask',
    '/create/task/watermelon', 'view.CreateWatermelonTask',
    '/complete/task/(.+)', 'view.CompleteTask',
    '/delete/task/(.+)', 'view.DeleteTask',
)

app = web.application(urls, globals())


def authenticator(handle):
    if not web.cookies().get('username') and web.ctx.path != '/login' and web.ctx.path != '/register':
        raise web.seeother('/login')
    return handle()


app.add_processor(authenticator)


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
            user = user_factory.create_user(username, password)

            web.setcookie('username', user.username)
            raise web.seeother('/')
        except InvalidCredentials:
            error = "Invalid Username or Password"
            return self.render_login_page(error)


class Logout:
    def __init__(self):
        pass

    def GET(self):
        web.setcookie('username', '', expires=-1)
        raise web.seeother('/login')


if __name__ == "__main__":
    app.run()
