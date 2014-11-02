class UserRepository:
    def __init__(self, storage_connection):
        self.storage_connection = storage_connection

    def create_user(self, username, password, salt):
        self.storage_connection.create_document(username, password, salt)

    def get_salt(self, username):
        return self.storage_connection.get_salt(username)

    def get_password(self, username):
        return self.storage_connection.get_password(username)
