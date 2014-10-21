import sys
from pymongo import MongoClient

class RewardRepository:
  def __init__(self):
    self.velocity_database = MongoClient('mongodb://localhost:27017').velocity

  def insert_reward(self, name, cost):
    rewards = self.velocity_database.rewards
    new_reward = { "Name" : name, "Cost" : cost }
    rewards.insert(new_reward)

  def view_all_rewards(self):
    rewards = self.velocity_database.rewards
    for reward in rewards.find(): 
      print(reward)

def main(arguments):
  repository = RewardRepository()
  if 'add' in arguments[1]:
    repository.insert_reward(arguments[2], arguments[3])
  elif 'viewall' in arguments[1]:
    repository.view_all_rewards()

if __name__ == "__main__":
  main(sys.argv)
