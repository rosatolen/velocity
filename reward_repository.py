import sys
from pymongo import MongoClient
from reward import *

class RewardRepository:
  def __init__(self):
    self.rewards = MongoClient('mongodb://localhost:27017').velocity.rewards

  def add(self, reward):
    self.rewards.insert({ "name": reward.name, "cost": reward.cost })

  def get_rewards(self):
    rewards = []
    for reward in self.rewards.find():
      rewards.append(Reward(reward['name'], reward['cost']))
    return rewards

  def view_all_rewards(self):
    for reward in self.rewards.find():
      print(reward)
      print(reward['name'])

def main(arguments):
  repository = RewardRepository()
  repository.view_all_rewards()

if __name__ == "__main__":
  main(sys.argv)
