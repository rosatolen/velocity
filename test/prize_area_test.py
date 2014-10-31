import mock
from nose import tools
from model.reward import Reward
from model.prize_area import PrizeArea, NotPurchasable
from model.repositories.reward_repository import RewardRepository
from model.bad_ass_points_purse import BadAssPointsPurse

mock_rewards_repository = mock.create_autospec(RewardRepository)
mock_bad_ass_points_purse = mock.create_autospec(BadAssPointsPurse)
prize_area = PrizeArea(mock_rewards_repository, mock_bad_ass_points_purse)


def test_deletion_of_reward_when_purhasing():
    reward_name = 'darn tough socks'

    prize_area.purchase(reward_name)

    mock_rewards_repository.remove.assert_called_with(reward_name)


def test_knowledge_that_it_contains_an_award():
    rewards = [Reward('kisses', 1000)]
    mock_rewards_repository.get_rewards.return_value = rewards
    task_name = 'kisses'

    tools.assert_true(prize_area.contains(task_name))


def test_returns_rewards():
    expected_rewards = [Reward('kisses', 1000)]
    mock_rewards_repository.get_rewards.return_value = expected_rewards

    actual_rewards = prize_area.get_rewards()

    tools.assert_equal(expected_rewards, actual_rewards)


def test_add_rewards():
    reward = Reward('kisses', 1000)

    prize_area.add(reward)

    mock_rewards_repository.add.assert_called_with(reward)


@tools.raises(NotPurchasable)
def test_throws_error_when_reward_cannot_be_purchased():
    rewards = [Reward('kisses', 1000)]
    mock_bad_ass_points_purse.total = 0
    mock_rewards_repository.get_rewards.return_value = rewards

    prize_area.purchase('kisses')
