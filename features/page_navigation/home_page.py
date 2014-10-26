from selenium.webdriver.common.by import By
from model.task import SnailTask
from model.task import QuailTask


class HomePage:
    def __init__(self, context):
        self.browser = context.browser

    def add_reward(self, reward):
        input_field = self.browser.find_element(By.NAME, 'new_reward_name')
        input_field.send_keys(reward.name)
        input_field = self.browser.find_element(By.NAME, 'new_reward_cost')
        input_field.send_keys(str(reward.cost))
        self.browser.find_element(By.NAME, 'submit_reward').click()

    def get_current_rewards(self):
        rewards = self.browser.find_elements(By.NAME, 'reward')
        costs = self.browser.find_elements(By.NAME, 'cost')

        actual_rewards = {}
        i = 0
        for reward in rewards:
            actual_rewards[reward.text] = int(costs[i].text)
            i += 1
        print actual_rewards
        return actual_rewards

    def add_snail_task(self, task):
        input_field = self.browser.find_element(By.NAME, 'new_snail_task_name')
        input_field.send_keys(task.name)
        self.browser.find_element(By.NAME, 'submit_snail_task').click()

    def add_quail_task(self, task):
        input_field = self.browser.find_element(By.NAME, 'new_quail_task_name')
        input_field.send_keys(task.name)
        self.browser.find_element(By.NAME, 'submit_quail_task').click()

    def get_current_tasks(self):
        snail_tasks = self.browser.find_elements(By.NAME, 'snail_task_name')
        quail_tasks = self.browser.find_elements(By.NAME, 'quail_task_name')
        print 'snails ' + str(snail_tasks)
        print 'quails ' + str(quail_tasks)
        actual_snail_tasks = []
        actual_quail_tasks = []
        for task in snail_tasks:
            actual_snail_tasks.append(SnailTask(task.text))
        for task in quail_tasks:
            actual_quail_tasks.append(QuailTask(task.text))
        return actual_snail_tasks, actual_quail_tasks
