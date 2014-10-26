from model.reward import *


class RewardRepository:
    def __init__(self, mongo_rewards_storage):
        self.mongo_rewards_storage = mongo_rewards_storage

    def add(self, reward):
        self.mongo_rewards_storage.insert_reward({"name": reward.name, "cost": reward.cost})

    def get_rewards(self):
        rewards = []
        for reward in self.mongo_rewards_storage.find_rewards():
            rewards.append(Reward(reward['name'], reward['cost']))
        return rewards
