from model.reward import *


class RewardRepository:
    def __init__(self, mongo_rewards_storage):
        self.rewards_storage = mongo_rewards_storage

    def add(self, reward):
        self.rewards_storage.insert_reward({"name": reward.name, "cost": reward.cost})

    def get_rewards(self):
        rewards = []
        for reward in self.rewards_storage.find_rewards():
            rewards.append(Reward(reward['name'], int(reward['cost'])))
        return rewards

    def remove(self, name):
        self.rewards_storage.remove_reward(name)

    def contains(self, name):
        for reward in self.rewards_storage.find_rewards():
            if reward['name'] == name:
                return True
        return False
