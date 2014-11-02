import hashlib


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


class InvalidCredentials(Exception):
    pass
