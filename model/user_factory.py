import hashlib
from model.user import User


class InvalidCredentials(Exception):
    pass


class UserFactory:
    def __init__(self, user_storage):
        self.user_storage = user_storage

    # misnomer! this is not creating a new user! this is getting one from the db
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
        points = self.user_storage.get_points(username)
        user = User(username, rewards, tasks, points)

        return user
