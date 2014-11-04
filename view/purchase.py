import web
from home import Home
from model.user import NotPurchasable
from model.repositories.user_repository import UserRepository
from model.repositories.mongo_wrapper import MongoWrapper


class PurchaseReward:
    def __init__(self):
        self.home_page = Home()

    def POST(self, reward_name):
        user = web.config.get('session')._initializer['user']
        try:
            print 'points ' + str(user.points)
            user.purchase(reward_name)

            user_repository = UserRepository(MongoWrapper())
            user_repository.save_state(user)
            raise web.seeother('/')
        except NotPurchasable:
            return self.home_page.render_home_page(user, error='Not enough points')
