import web
from home import Home
from model.user_repository import UserRepository, UserFactory, MongoWrapper


class DeleteTask:
    def __init__(self):
        self.home = Home()

    def POST(self, task_name):
        user_factory = UserFactory(UserRepository(MongoWrapper()))
        user = user_factory.find_user(web.cookies().get('username'))

        delete_task_form = self.home.delete_task_form
        if not delete_task_form.validates():
            return self.home.render_home_page(user)

        user.delete_task(task_name)

        user_repository = UserRepository(MongoWrapper())
        user_repository.save_state(user)

        raise web.seeother('/')


class DeleteReward:
    def __init__(self):
        self.home = Home()

    def POST(self, reward_name):
        user_factory = UserFactory(UserRepository(MongoWrapper()))
        user = user_factory.find_user(web.cookies().get('username'))

        delete_reward_form = self.home.delete_reward_form
        if not delete_reward_form.validates():
            return self.home.render_home_page(user)

        user.delete_reward(reward_name)

        user_repository = UserRepository(MongoWrapper())
        user_repository.save_state(user)

        raise web.seeother('/')
