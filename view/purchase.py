import web
from home import Home
from model.user import NotPurchasable
from model.user_repository import UserRepository, MongoWrapper, UserFactory


class PurchaseReward:
    def __init__(self):
        self.home_page = Home()

    def POST(self, reward_name):
        user_factory = UserFactory(UserRepository(MongoWrapper()))
        user = user_factory.find_user(web.cookies().get('username'))

        try:
            user.purchase(reward_name)

            user_repository = UserRepository(MongoWrapper())
            user_repository.save_state(user)

            raise web.seeother('/')
        except NotPurchasable:
            return self.home_page.render_home_page(user, error='Not enough points')
