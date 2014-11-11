from datetime import date, datetime
from pytz import timezone
import mock
from nose import tools
from model.user import User
from model.reward import Reward
from model.task import *
from model.purse import Purse
from model.habit import Habit
from model.user_repository import UserRepository, UserFactory


mock_user_storage = mock.create_autospec(UserRepository)
user_factory = UserFactory(mock_user_storage)
timezone = timezone('US/Pacific')


def test_validation_around_creating_users():
    mock_user_storage.get_salt.return_value = 'salt'
    mock_user_storage.get_password.return_value = '13601bda4ea78e55a07b98866d2be6be0744e3866f13c00c811cab608a28f322'

    user_factory.create_user('username', 'password')

    mock_user_storage.get_salt.assert_called_with('username')
    mock_user_storage.get_password.assert_called_with('username')


def test_creating_user():
    mock_user_storage.get_salt.return_value = 'salt'
    mock_user_storage.get_password.return_value = '13601bda4ea78e55a07b98866d2be6be0744e3866f13c00c811cab608a28f322'

    rewards = [Reward('kisses', 100), Reward('trip', 1000)]
    tasks = [SnailTask('send email'), QuailTask('create presentation'), WatermelonTask('read a book')]
    purse = Purse(0, 0, date.today(), timezone)
    habits = [Habit('run')]

    mock_user_storage.get_tasks.return_value = tasks
    mock_user_storage.get_rewards.return_value = rewards
    mock_user_storage.get_purse.return_value = purse
    mock_user_storage.get_habits.return_value = habits

    expected_user = User('username', rewards, tasks, habits, purse)

    actual_user = user_factory.create_user('username', 'password')

    tools.assert_equal(expected_user, actual_user)


def test_find_existing_user():
    username = 'username'
    rewards = [Reward('kisses', 100), Reward('trip', 1000)]
    tasks = [SnailTask('send email'), QuailTask('create presentation'), WatermelonTask('read a book')]
    purse = Purse(0, 0, date.today(), timezone)
    habits = [Habit('run')]

    mock_user_storage.get_tasks.return_value = tasks
    mock_user_storage.get_rewards.return_value = rewards
    mock_user_storage.get_purse.return_value = purse
    mock_user_storage.get_habits.return_value = habits

    expected_user = User(username, rewards, tasks, habits, purse)

    actual_user = user_factory.find_user(username)

    tools.assert_equal(expected_user, actual_user)
