import hashlib


class User:
    def __init__(self, username, password, user_storage):
        user_storage.get_salt(username)
        #check hash here

        self.username = username
        self.password = password
