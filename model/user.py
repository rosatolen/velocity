import hashlib


class User:
    def __init__(self, username, password, user_storage):
        try:
            user_storage.get_salt(username)
            self.username = username
            self.password = password
        except TypeError:
            raise InvalidCredentials


class InvalidCredentials(Exception):
    pass
