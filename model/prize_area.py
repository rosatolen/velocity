class PrizeArea:
    def __init__(self, reward_repository, bad_ass_points_purse):
        self.bad_ass_points_purse = bad_ass_points_purse
        self.reward_repository = reward_repository
        self.rewards = reward_repository.get_rewards()

    def purchase(self, reward_name):
        for reward in self.rewards:
            if reward.name == reward_name:
                self.bad_ass_points_purse.subtract_reward_cost(reward.cost)
        self.reward_repository.remove(reward_name)