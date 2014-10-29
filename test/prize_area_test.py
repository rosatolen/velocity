import mock
from nose import tools
from model.reward import Reward
from model.prize_area import PrizeArea
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
