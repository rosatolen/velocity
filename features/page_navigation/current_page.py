from nose import tools
from selenium.webdriver.common.by import By
from model.task import SnailTask, QuailTask, WatermelonTask
from model.reward import Reward


class CurrentPage:
    def __init__(self, context):
        self.browser = context.browser

    def click_on_registration_link(self):
        self.browser.find_element(By.NAME, 'register').click()

    def click_on_logout_link(self):
        self.browser.find_element(By.NAME, 'logout').click()

    def get_validation_error_messages(self):
        error_messages = []
        for error_message in self.browser.find_elements(By.CLASS_NAME, 'wrong'):
            error_messages.append(error_message.text)
        return error_messages

    def get_upper_level_error_messages(self):
        return self.browser.find_element(By.NAME, 'error').text

    def delete_task(self):
        self.browser.find_element(By.NAME, 'delete_task').click()
