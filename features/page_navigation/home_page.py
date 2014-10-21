from selenium.webdriver.common.by import By

def add_reward(context, reward):
  inputField = context.browser.find_element(By.ID, 'new_reward_name')
  inputField.send_keys(reward.name)
  inputField = context.browser.find_element(By.ID, 'new_reward_cost')
  inputField.send_keys(str(reward.cost))
