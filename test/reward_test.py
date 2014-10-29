from nose import tools
from model.reward import Reward


def test_equality():
    reward1 = Reward('kisses', 1000)
    reward2 = Reward('kisses', 1000)
    tools.assert_equal(reward1, reward2)
