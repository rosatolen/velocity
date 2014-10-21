from pymongo import MongoClient

def after_scenario(context, scenario):
  velocity_database = MongoClient('mongodb://localhost:27017').velocity
  velocity_database.rewards.drop()
  velocity_database.tasks.drop()
