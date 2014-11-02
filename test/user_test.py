import mock
from model.repositories.user_repository import UserRepository
from model.user import User

mock_user_storage = mock.create_autospec(UserRepository)


def test_creation():
    User('username', 'password', mock_user_storage)

    mock_user_storage.get_salt.assert_called_with('username')
