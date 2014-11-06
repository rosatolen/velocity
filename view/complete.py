import web
from home import Home
from model.user_repository import UserRepository, MongoWrapper, UserFactory


class CompleteTask:
    def __init__(self):
        self.home = Home()

    def POST(self, task_name):
        user_factory = UserFactory(UserRepository(MongoWrapper()))
        user = user_factory.find_user(web.cookies().get('username'))

        complete_task_form = self.home.complete_task_form
        if not complete_task_form.validates():
            return self.home.render_home_page(user)

        user.complete(task_name)

        user_repository = UserRepository(MongoWrapper())
        user_repository.save_state(user)

        raise web.seeother('/')
