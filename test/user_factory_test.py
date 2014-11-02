import mock
from nose import tools
from model.user_factory import UserFactory
from model.user import User
from model.repositories.user_repository import UserRepository


mock_user_storage = mock.create_autospec(UserRepository)
user_factory = UserFactory(mock_user_storage)


def test_validation_around_creating_users():
    mock_user_storage.get_salt.return_value = 'salt'
    mock_user_storage.get_password.return_value = '13601bda4ea78e55a07b98866d2be6be0744e3866f13c00c811cab608a28f322'

    user_factory.create_user('username', 'password')

    mock_user_storage.get_salt.assert_called_with('username')
    mock_user_storage.get_password.assert_called_with('username')


def test_creating_user():
    mock_user_storage.get_salt.return_value = 'salt'
    mock_user_storage.get_password.return_value = '13601bda4ea78e55a07b98866d2be6be0744e3866f13c00c811cab608a28f322'
    #expected_user = User(prize_area, todo_list, bad_ass_points_purse)

    #actual_user = user_factory.create_user('username', 'password')
