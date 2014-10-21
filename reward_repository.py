import sys
from pymongo import MongoClient

class RewardRepository:
  def __init__(self):
    self.rewards = MongoClient('mongodb://localhost:27017').velocity.rewards

  def insert_reward(self, name, cost):
    new_reward = { "Name" : name, "Cost" : cost }
    self.rewards.insert(new_reward)

  def view_all_rewards(self):
    for reward in self.rewards.find():
      print(reward)

def main(arguments):
  repository = RewardRepository()
  if 'add' in arguments[1]:
    repository.insert_reward(arguments[2], arguments[3])
  elif 'viewall' in arguments[1]:
    repository.view_all_rewards()

if __name__ == "__main__":
  main(sys.argv)
