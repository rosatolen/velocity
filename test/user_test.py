import mock
from model.repositories.user_repository import UserRepository
from model.user import User

mock_user_storage = mock.create_autospec(UserRepository)


def test_creation():
    mock_user_storage.get_salt.return_value = 'salt'
    mock_user_storage.get_password.return_value = '13601bda4ea78e55a07b98866d2be6be0744e3866f13c00c811cab608a28f322'

    User('username', 'password', mock_user_storage)

    mock_user_storage.get_salt.assert_called_with('username')
    mock_user_storage.get_password.assert_called_with('username')
