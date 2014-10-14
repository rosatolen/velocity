import mock
import unittest
from repository import Repository

class RewardsRepository:
  def __init__(self):
    self.repository = Repository()

  def insert_reward():
    repository.save_reward("Reward Name", 100)




class RewardsRepositoryTest(unittest.TestCase):

  @mock.patch('this.repository')
  def testStoresResult(self, repository):
    insert_reward()
    repository.save_reward.assert_called_with("Reward Name", 100)

def main():
  unittest.main()

if __name__ == '__main__':
  main()
