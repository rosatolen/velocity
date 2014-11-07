from nose import tools
from model.user import User, NotPurchasable
from model.task import *
from model.reward import Reward


def test_complete_task():
    task = QuailTask('read')
    user = User('username', [], [task], 0)

    user.complete('read')

    tools.assert_equal([], user.tasks)
    tools.assert_equal(8, user.points)


def test_purchase_reward():
    user = User('username', [Reward('kisses', 1000)], [], 1000)

    user.purchase('kisses')

    tools.assert_equal(0, user.points)
    tools.assert_equal([], user.rewards)


@tools.raises(NotPurchasable)
def test_unpurchasable_reward():
    user = User('username', [Reward('kisses', 1000)], [], 0)

    user.purchase('kisses')


def test_user_has_reward():
    user = User('username', [Reward('kisses', 1000)], [], 1000)

    tools.assert_true(user.has_reward_named('kisses'))
    tools.assert_false(user.has_reward_named('trip to Singapore'))


def test_user_has_task():
    user = User('username', [Reward('kisses', 1000)], [SnailTask('write an email')], 1000)

    tools.assert_true(user.has_task_named('write an email'))
    tools.assert_false(user.has_task_named('read a book'))


def test_user_deletes_task():
    task_name = 'write an email'
    user = User('username', [Reward('kisses', 1000)], [SnailTask(task_name)], 1000)

    user.delete_task(task_name)

    tools.assert_false(user.has_task_named(task_name))


def test_user_deletes_reward():
    reward_name = 'kisses'
    user = User('username', [Reward(reward_name, 1000)], [SnailTask('write an email')], 1000)

    user.delete_reward(reward_name)

    tools.assert_false(user.has_reward_named(reward_name))
