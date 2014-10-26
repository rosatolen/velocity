import mock
from model.reward_repository import RewardRepository
from model.reward import Reward
from model.mongo_wrapper import MongoWrapper


def test_call_to_mongo_when_adding_a_reward():
    mock_rewards_storage = mock.create_autospec(MongoWrapper)
    reward_repo = RewardRepository(mock_rewards_storage)

    reward = Reward('reward', 100)
    reward_repo.add(reward)

    mock_rewards_storage.insert_reward.assert_called_with({"name": reward.name, "cost": reward.cost})


def test_call_to_mongo_when_getting_rewards():
    mock_rewards_storage = mock.create_autospec(MongoWrapper)
    reward_repo = RewardRepository(mock_rewards_storage)

    reward_repo.get_rewards()

    mock_rewards_storage.find_rewards().assert_called()
