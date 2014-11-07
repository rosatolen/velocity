from model.task import *


class NotPurchasable(Exception):
    pass


class User:
    def __init__(self, username, rewards, tasks, points):
        self.username = username
        self.rewards = rewards
        self.tasks = tasks
        self.points = int(points)

    def complete(self, task_name):
        for task in self.tasks:
            if task.name == task_name:
                self.points += task.size
                self.tasks.remove(task)

    def purchase(self, reward_name):
        for reward in self.rewards:
            if reward.name == reward_name:
                if self.points < reward.cost:
                    raise NotPurchasable
                else:
                    self.rewards.remove(reward)
                    self.points -= reward.cost

    def has_reward_named(self, reward_name):
        for reward in self.rewards:
            if reward.name == reward_name:
                return True
        return False

    def has_task_named(self, task_name):
        for task in self.tasks:
            if task.name == task_name:
                return True
        return False

    def delete_task(self, task_name):
        for task in self.tasks:
            if task.name == task_name:
                self.tasks.remove(task)

    def delete_reward(self, reward_name):
        for reward in self.rewards:
            if reward.name == reward_name:
                self.rewards.remove(reward)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.__dict__ == other.__dict__
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)
