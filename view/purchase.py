import web
from home import Home
from model.prize_area import PrizeArea, NotPurchasable
from model.bad_ass_points_purse import BadAssPointsPurse
from model.repositories.reward_repository import RewardRepository
from model.repositories.bad_ass_points_repository import BadAssPointsRepository
from model.repositories.mongo_wrapper import MongoWrapper


class PurchaseReward:
    def __init__(self):
        self.prize_area = PrizeArea(RewardRepository(MongoWrapper()),
                                    BadAssPointsPurse(BadAssPointsRepository(MongoWrapper())))
        self.home_page = Home()

    def POST(self, reward_name):
        try:
            self.prize_area.purchase(reward_name)
            raise web.seeother('/')
        except NotPurchasable:
            return self.home_page.render_home_page(error='Not enough points')
