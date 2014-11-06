from pymongo import MongoClient
from selenium import webdriver
from page_navigation import *
import subprocess
from behave import use_step_matcher

use_step_matcher("parse")


def before_all(context):
    print '*** Starting Velocity on localhost:1234 ***'
    clean_database()
    context.server = subprocess.Popen(["python app.py 1234"], stdout=subprocess.PIPE, shell=True)
    context.browser = webdriver.Chrome()
    context.current_page = CurrentPage(context)


def before_scenario(context, scenario):
    context.browser.get('localhost:1234/logout')
    context.browser.get('localhost:1234')
    context.expected_snail_tasks = []
    context.expected_quail_tasks = []
    context.expected_rewards = []


def after_all(context):
    context.server.terminate()
    context.browser.quit()


def after_scenario(context, scenario):
    clean_database()


def clean_database():
    velocity_database = MongoClient('mongodb://localhost:27017').velocity
    velocity_database.users.drop()
