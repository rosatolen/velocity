import hashlib


class User:
    def __init__(self, username, password, user_storage):

        try:
            salt = user_storage.get_salt(username)
        except TypeError:
            raise InvalidCredentials

        possible_password = hashlib.sha256(salt + password).hexdigest()
        existing_password = user_storage.get_password(username)
        if possible_password != existing_password:
            raise InvalidCredentials

        self.username = username


class InvalidCredentials(Exception):
    pass
