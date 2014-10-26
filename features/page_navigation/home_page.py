from selenium.webdriver.common.by import By
from task import SnailTask

class HomePage:
  def __init__(self, context):
    self.browser = context.browser

  def add_reward(self, reward):
    inputField = self.browser.find_element(By.NAME, 'new_reward_name')
    inputField.send_keys(reward.name)
    inputField = self.browser.find_element(By.NAME, 'new_reward_cost')
    inputField.send_keys(str(reward.cost))
    self.browser.find_element(By.NAME, 'submit_reward').click()

  def get_current_rewards(self):
    rewards = self.browser.find_elements(By.NAME, 'reward')
    costs = self.browser.find_elements(By.NAME, 'cost')

    actual_rewards = {}
    i = 0
    for reward in rewards: 
      actual_rewards[reward.text] = int(costs[i].text)
      i = i + 1
    print actual_rewards
    return actual_rewards

  def add_task(self, task):
    inputField = self.browser.find_element(By.NAME, 'new_snail_task_name')
    inputField.send_keys(task.name)
    self.browser.find_element(By.NAME, 'submit_snail_task').click()

  def get_current_tasks(self):
    tasks = self.browser.find_elements(By.NAME, 'task_name')
    actual_tasks = []
    for task in tasks:
      actual_tasks.append(SnailTask(task.text))
    return actual_tasks
