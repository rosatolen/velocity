from selenium.webdriver.common.by import By

class HomePage:
  def __init__(self, context):
    self.browser = context.browser

  def add_reward(self, reward):
    inputField = self.browser.find_element(By.NAME, 'new_reward_name')
    inputField.send_keys(reward.name)
    inputField = self.browser.find_element(By.NAME, 'new_reward_cost')
    inputField.send_keys(str(reward.cost))
    self.browser.find_element(By.TAG_NAME, 'button').click()

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
