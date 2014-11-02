import mock
from nose import tools
from model.repositories.user_repository import UserRepository
from model.repositories.mongo_wrapper import MongoWrapper

mock_user_storage = mock.create_autospec(MongoWrapper)
user_repo = UserRepository(mock_user_storage)


def test_call_to_create_user():
    user_repo.create_user('username', 'password', 'salt')

    mock_user_storage.create_document.assert_called_with('username', 'password', 'salt')


def test_call_to_get_salt_for_user():
    mock_user_storage.get_salt.return_value = '1234'

    tools.assert_equal('1234', user_repo.get_salt('username'))