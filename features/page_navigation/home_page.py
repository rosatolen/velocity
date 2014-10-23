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

  def assert_reward_exists(self, reward):
    self.browser.findElement(By.NAME, 'rewards')
