from pymongo import MongoClient
from selenium import webdriver
from page_navigation import *
import subprocess


def before_all(context):
    print '*** Starting Velocity on localhost:1234 ***'
    clean_database()
    context.server = subprocess.Popen(["python view.py 1234"], stdout=subprocess.PIPE, shell=True)
    context.browser = webdriver.Chrome()
    context.home_page = HomePage(context)


def before_scenario(context, scenario):
    context.browser.get('localhost:1234')


def after_all(context):
    context.server.terminate()
    context.browser.quit()


def after_scenario(context, scenario):
    clean_database()


def clean_database():
    velocity_database = MongoClient('mongodb://localhost:27017').velocity
    velocity_database.rewards.drop()
    velocity_database.tasks.drop()
