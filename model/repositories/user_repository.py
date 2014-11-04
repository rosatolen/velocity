from model.task import *
from model.reward import Reward


class UserRepository:
    def __init__(self, storage_connection):
        self.storage_connection = storage_connection

    def create_user(self, username, password, salt):
        self.storage_connection.insert({
            'username': username,
            'password': password,
            'salt': salt,
            'points': 0,
            'rewards': [],
            'tasks': []
        })

    def get_salt(self, username):
        return self.storage_connection.get_salt(username)

    def get_password(self, username):
        return self.storage_connection.get_password(username)

    def get_points(self, username):
        db_user_obj = self.storage_connection.find_one({'username': username})
        return int(db_user_obj['points'])

    def get_tasks(self, username):
        db_user = self.storage_connection.find_one({'username': username})
        if not db_user['tasks']:
            return []
        else:
            tasks = []
            for db_task in db_user['tasks']:
                tasks.append(create_task(db_task))
            return tasks

    def get_rewards(self, username):
        db_user = self.storage_connection.find_one({'username': username})
        if not db_user['rewards']:
            return []
        else:
            rewards = []
            for db_reward in db_user['rewards']:
                rewards.append(Reward(db_reward['name'], db_reward['cost']))
            return rewards

    def save_state(self, user):
        user_query = {'username': user.username}

        # DEBT use this instead of calling self.get_*
        db_user = self.storage_connection.find_one(user_query)

        username = db_user['username']
        password = db_user['password']
        salt = db_user['salt']

        changed_total = find_changed(db_user['points'], user.points)

        current_rewards = self.get_rewards(user.username)
        changed_rewards = find_changed(current_rewards, user.rewards)
        dict_rewards = []
        for reward in changed_rewards:
            dict_rewards.append(dict(zip(('name', 'cost'), (reward.name, reward.cost))))

        current_tasks = self.get_tasks(user.username)
        changed_tasks = find_changed(current_tasks, user.tasks)
        dict_tasks = []
        for task in changed_tasks:
            dict_tasks.append(dict(zip(('name', 'size'), (task.name, task.size))))

        self.storage_connection.remove(user_query)
        self.storage_connection.insert({
            'username': username,
            'password': password,
            'salt': salt,
            'points': changed_total,
            'rewards': dict_rewards,
            'tasks': dict_tasks
        })


def find_changed(original, new):
    if original == new:
        return original
    else:
        return new


def create_task(db_task):
    if db_task['size'] == 'snail':
        return SnailTask(db_task['name'])
    elif db_task['size'] == 'quail':
        return QuailTask(db_task['name'])
    else:
        return WatermelonTask(db_task['name'])
