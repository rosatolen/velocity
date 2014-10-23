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

  def insert_reward(self, name, cost):
    new_reward = { "name" : name, "Cost" : cost }
    self.rewards.insert(new_reward)

  def view_all_rewards(self):
    for reward in self.rewards.find():
      print(reward)
      print(reward['name'])

def main(arguments):
  repository = RewardRepository()
  if 'add' in arguments[1]:
    repository.insert_reward(arguments[2], arguments[3])
  elif 'viewall' in arguments[1]:
    repository.view_all_rewards()

if __name__ == "__main__":
  main(sys.argv)
