from pytz import timezone
from nose import tools
from model.user import User, NotPurchasable
from model.task import SnailTask, QuailTask, WatermelonTask
from model.reward import Reward
from model.purse import Purse
from model.habit import Habit
from datetime import date


pacific_timezone = timezone('US/Pacific')
todays_empty_purse = Purse(0, 0, date.today(), pacific_timezone)


def test_complete_quail_task():
    task = QuailTask('read')
    user = User('username', [], [task], [], Purse(0, 0, date.today(), pacific_timezone))

    user.complete_task('read')

    tools.assert_equal([], user.tasks)
    tools.assert_equal(8, user.purse.total)
    tools.assert_equal(8, user.purse.todays_total)

def test_complete_watermelon_task():
    task = WatermelonTask('read a book')
    user = User('username', [], [task], [], Purse(0, 0, date.today(), pacific_timezone))

    user.complete_task('read a book')

    tools.assert_equal([], user.tasks)
    tools.assert_equal(55, user.purse.total)
    tools.assert_equal(55, user.purse.todays_total)

def test_purchase_reward():
    user = User('username', [Reward('kisses', 1000)], [], [], Purse(1000, 10, date.today(), pacific_timezone))

    user.purchase('kisses')

    tools.assert_equal(0, user.purse.total)
    tools.assert_equal(10, user.purse.todays_total)
    tools.assert_equal([], user.rewards)


@tools.raises(NotPurchasable)
def test_unpurchasable_reward():
    user = User('username', [Reward('kisses', 1000)], [], [], todays_empty_purse)

    user.purchase('kisses')


def test_user_has_reward():
    user = User('username', [Reward('kisses', 1000)], [], [], Purse(1000, 1000, date.today(), pacific_timezone))

    tools.assert_true(user.has_reward_named('kisses'))
    tools.assert_false(user.has_reward_named('trip to Singapore'))


def test_user_has_task():
    user = User('username', [Reward('kisses', 1000)], [SnailTask('write an email')], [], 1000)

    tools.assert_true(user.has_task_named('write an email'))
    tools.assert_false(user.has_task_named('read a book'))


def test_user_deletes_task():
    task_name = 'write an email'
    user = User('username', [Reward('kisses', 1000)], [SnailTask(task_name)], [], todays_empty_purse)

    user.delete_task(task_name)

    tools.assert_false(user.has_task_named(task_name))


def test_user_deletes_reward():
    reward_name = 'kisses'
    user = User('username', [Reward(reward_name, 1000)], [SnailTask('write an email')], [], todays_empty_purse)

    user.delete_reward(reward_name)

    tools.assert_false(user.has_reward_named(reward_name))


def test_user_completes_habit():
    habit_name = 'run'
    empty_purse = Purse(0, 0, date.today(), pacific_timezone)
    user = User('username', [], [], [Habit(habit_name)], empty_purse)

    user.complete_habit(habit_name)

    tools.assert_equal(1, user.purse.total)
    tools.assert_equal(1, user.purse.todays_total)
