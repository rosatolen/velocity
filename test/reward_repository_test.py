import mock
from model.repositories.reward_repository import RewardRepository
from model.reward import Reward
from model.repositories.mongo_wrapper import MongoWrapper


mock_rewards_storage = mock.create_autospec(MongoWrapper)
reward_repo = RewardRepository(mock_rewards_storage)


def test_call_to_mongo_when_adding_a_reward():
    reward = Reward('reward', 100)

    reward_repo.add(reward)

    mock_rewards_storage.insert_reward.assert_called_with({"name": reward.name, "cost": reward.cost})


def test_call_to_mongo_when_getting_rewards():
    reward_repo.get_rewards()

    mock_rewards_storage.find_rewards().assert_called()


def test_call_to_reward_storage_when_removing_reward():
    reward_name = 'darn tough socks'

    reward_repo.remove(reward_name)

    mock_rewards_storage.remove_reward.assert_called_with(reward_name)
