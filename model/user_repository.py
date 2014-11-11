import os
import hashlib
import web
from pytz import timezone
from datetime import datetime, date
from pymongo import MongoClient
from model.task import *
from model.reward import Reward
from model.user import User
from model.purse import Purse
from model.habit import Habit


class InvalidCredentials(Exception):
    pass


class UserExists(Exception):
    pass


class UserFactory:
    def __init__(self, user_storage):
        self.user_storage = user_storage

    def create_user(self, username, password):
        try:
            salt = self.user_storage.get_salt(username)
        except TypeError:
            raise InvalidCredentials

        possible_password = hashlib.sha256(salt + password).hexdigest()
        existing_password = self.user_storage.get_password(username)
        if possible_password != existing_password:
            raise InvalidCredentials

        rewards = self.user_storage.get_rewards(username)
        tasks = self.user_storage.get_tasks(username)
        purse = self.user_storage.get_purse(username)
        habits = self.user_storage.get_habits(username)
        user = User(username, rewards, tasks, habits, purse)

        return user

    def find_user(self, username):
        rewards = self.user_storage.get_rewards(username)
        tasks = self.user_storage.get_tasks(username)
        purse = self.user_storage.get_purse(username)
        habits = self.user_storage.get_habits(username)
        return User(username, rewards, tasks, habits, purse)


class UserRepository:
    def __init__(self, storage_connection):
        self.storage_connection = storage_connection

    def create_user(self, username, password, salt):
        username = normalize(username)

        if self.storage_connection.find_one({'username': username}):
            raise UserExists

        self.storage_connection.insert({
            'username': username,
            'password': password,
            'salt': salt,
            'purse': {
                'total': 0,
                'todays_total': 0,
                'last_updated_date': date_at_midnight(date.today())
            },
            'rewards': [],
            'tasks': [],
            'habits': []
        })

    def get_salt(self, username):
        username = normalize(username)
        return self.storage_connection.get_salt(username)

    def get_password(self, username):
        username = normalize(username)
        return self.storage_connection.get_password(username)

    def get_purse(self, username):
        username = normalize(username)
        db_purse = self.storage_connection.find_one({'username': username})['purse']
        pacific = timezone('US/Pacific')
        return Purse(db_purse['total'], db_purse['todays_total'], db_purse['last_updated_date'].date(), pacific)

    def get_tasks(self, username):
        username = normalize(username)
        db_user = self.storage_connection.find_one({'username': username})
        if not db_user['tasks']:
            return []
        else:
            tasks = []
            for db_task in db_user['tasks']:
                tasks.append(create_task(db_task))
            return tasks

    def get_rewards(self, username):
        username = normalize(username)
        db_user = self.storage_connection.find_one({'username': username})
        if not db_user['rewards']:
            return []
        else:
            rewards = []
            for db_reward in db_user['rewards']:
                rewards.append(Reward(db_reward['name'], db_reward['cost']))
            return rewards

    def get_habits(self, username):
        username = normalize(username)
        db_user = self.storage_connection.find_one({'username': username})
        if not db_user['habits']:
            return []
        else:
            habits = []
            for db_habit in db_user['habits']:
                habits.append(Habit(db_habit['name']))
            return habits

    def save_state(self, user):
        user_query = {'username': normalize(user.username)}
        db_user = self.storage_connection.find_one(user_query)

        username = db_user['username']
        password = db_user['password']
        salt = db_user['salt']

        changed_todays_total, changed_total, changed_updated_day = self.get_changed_purse_data(db_user, user)
        dict_rewards = self.create_rewards_dict(user)
        dict_tasks = self.create_tasks_dict(user)
        dict_habits = self.create_habits_dict(user)

        self.storage_connection.remove(user_query)
        self.storage_connection.insert({
            'username': username,
            'password': password,
            'salt': salt,
            'purse': {
                'total': changed_total,
                'todays_total': changed_todays_total,
                'last_updated_date': changed_updated_day
            },
            'rewards': dict_rewards,
            'tasks': dict_tasks,
            'habits': dict_habits
        })

    def create_habits_dict(self, user):
        current_habits = self.get_habits(user.username)
        changed_habits = find_changed(current_habits, user.habits)
        dict_habits = []
        for habit in changed_habits:
            dict_habits.append(dict([('name', habit.name)]))
        return dict_habits

    def create_tasks_dict(self, user):
        current_tasks = self.get_tasks(user.username)
        changed_tasks = find_changed(current_tasks, user.tasks)
        dict_tasks = []
        for task in changed_tasks:
            dict_tasks.append(dict(zip(('name', 'size'), (task.name, size(task)))))
        return dict_tasks

    def create_rewards_dict(self, user):
        current_rewards = self.get_rewards(user.username)
        changed_rewards = find_changed(current_rewards, user.rewards)
        dict_rewards = []
        for reward in changed_rewards:
            dict_rewards.append(dict(zip(('name', 'cost'), (reward.name, reward.cost))))
        return dict_rewards

    def get_changed_purse_data(self, db_user, user):
        changed_total = find_changed(db_user['purse']['total'], user.purse.total)
        changed_todays_total = find_changed(db_user['purse']['todays_total'], user.purse.todays_total)
        changed_updated_day = find_changed(db_user['purse']['last_updated_date'],
                                           date_at_midnight(user.purse.last_updated_day))
        return changed_todays_total, changed_total, changed_updated_day


def date_at_midnight(day):
    return datetime.combine(day, datetime.min.time())


def normalize(value):
    return value.lower()


def find_changed(original, new):
    if original == new:
        return original
    else:
        return new


def size(task):
    if isinstance(task, SnailTask):
        return 'snail'
    elif isinstance(task, QuailTask):
        return 'quail'
    else:
        return 'watermelon'


def create_task(db_task):
    if db_task['size'] == 'snail':
        return SnailTask(db_task['name'])
    elif db_task['size'] == 'quail':
        return QuailTask(db_task['name'])
    else:
        return WatermelonTask(db_task['name'])


class MongoWrapper:
    def __init__(self):
        try:
            mongolab_uri = os.environ['MONGOLAB_URI']
            db = MongoClient(mongolab_uri)
            self.users = db.get_default_database().users
        except KeyError:
            client = MongoClient('mongodb://localhost:27017')
            self.users = client.velocity.users

    def get_salt(self, username):
        user = self.users.find_one({'username': username})
        return user['salt']

    def get_password(self, username):
        user = self.users.find_one({'username': username})
        return user['password']

    def insert(self, query):
        self.users.insert(query)

    def remove(self, query):
        self.users.remove(query)

    def find_one(self, query):
        return self.users.find_one(query)
