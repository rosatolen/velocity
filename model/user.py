from model.task import *


class NotPurchasable(Exception):
    pass


class User:
    def __init__(self, username, rewards, tasks, habits, purse):
        self.username = username
        self.rewards = rewards
        self.tasks = tasks
        self.habits = habits
        self.purse = purse

    def complete_task(self, task_name):
        for task in self.tasks:
            if task.name == task_name:
                self.purse.add(task.size)
                self.tasks.remove(task)

    def purchase(self, reward_name):
        for reward in self.rewards:
            if reward.name == reward_name:
                if self.purse.total < reward.cost:
                    raise NotPurchasable
                else:
                    self.rewards.remove(reward)
                    self.purse.subtract(reward.cost)

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

    def complete_habit(self, habit_name):
        for habit in self.habits:
            if habit.name == habit_name:
                self.purse.add(1)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.__dict__ == other.__dict__
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)
