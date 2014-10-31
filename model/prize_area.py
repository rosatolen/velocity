class PrizeArea:
    def __init__(self, reward_repository, bad_ass_points_purse):
        self.bad_ass_points_purse = bad_ass_points_purse
        self.reward_repository = reward_repository

    def purchase(self, reward_name):
        for reward in self.reward_repository.get_rewards():
            if reward.name == reward_name:
                if self.bad_ass_points_purse.total < reward.cost:
                    raise NotPurchasable()

                self.bad_ass_points_purse.subtract_reward_cost(reward.cost)
        self.reward_repository.remove(reward_name)

    def contains(self, reward_name):
        return self.reward_repository.contains(reward_name)

    def get_rewards(self):
        return self.reward_repository.get_rewards()

    def add(self, reward):
        self.reward_repository.add(reward)


class NotPurchasable(Exception):
    pass
