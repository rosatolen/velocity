from pymongo import MongoClient
from selenium import webdriver
import subprocess

def before_all(context):
  print '*** Starting Velocity on localhost:1234 ***'
  context.server = subprocess.Popen(["python view.py 1234"], stdout=subprocess.PIPE, shell=True)
  context.browser = webdriver.Chrome()

def after_all(context):
  context.server.terminate()
  context.browser.quit()

def after_scenario(context, scenario):
  velocity_database = MongoClient('mongodb://localhost:27017').velocity
  velocity_database.rewards.drop()
  velocity_database.tasks.drop()
