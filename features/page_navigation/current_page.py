from nose import tools
from selenium.webdriver.common.by import By
from model.task import SnailTask, QuailTask, WatermelonTask
from model.reward import Reward


class CurrentPage:
    def __init__(self, context):
        self.browser = context.browser

    def navigate_to_home_page(self):
        self.browser.get('localhost:1234')

    def assert_that_current_page_is_login_page(self):
        current_page_name = self.browser.find_element(By.NAME, 'page_name').text
        tools.assert_equal('Login', current_page_name)

    def navigate_to_registration_page(self):
        self.browser.get('localhost:1234/register')

    def click_on_registration_link(self):
        self.browser.find_element(By.NAME, 'register').click()

    def register(self, username, password, repassword):
        input_field = self.browser.find_element(By.NAME, 'username')
        input_field.send_keys(username)
        input_field = self.browser.find_element(By.NAME, 'password')
        input_field.send_keys(password)
        input_field = self.browser.find_element(By.NAME, 'retype_password')
        input_field.send_keys(repassword)
        self.browser.find_element(By.NAME, 'register').click()

    def navigate_to_login_page(self):
        self.browser.get('localhost:1234/login')

    def login(self, username, password):
        input_field = self.browser.find_element(By.NAME, 'username')
        input_field.send_keys(username)
        input_field = self.browser.find_element(By.NAME, 'password')
        input_field.send_keys(password)
        self.browser.find_element(By.NAME, 'login').click()

    def click_on_logout_link(self):
        self.browser.find_element(By.NAME, 'logout').click()

    def assert_that_current_page_is_home_page(self):
        bad_ass_points = self.browser.find_element(By.NAME, 'bad_ass_points').text
        tools.assert_true('Bad Ass Points Total:' in bad_ass_points)

    def add_reward(self, reward):
        input_field = self.browser.find_element(By.NAME, 'new_reward_name')
        input_field.send_keys(reward.name)
        input_field = self.browser.find_element(By.NAME, 'new_reward_cost')
        input_field.send_keys(reward.cost)
        self.browser.find_element(By.NAME, 'submit_reward').click()

    def get_rewards(self):
        rewards = self.browser.find_elements(By.NAME, 'reward')
        costs = self.browser.find_elements(By.NAME, 'cost')
        actual_rewards = []
        for reward, cost in zip(rewards, costs):
            new_reward = Reward(reward.text, int(cost.text))
            actual_rewards.append(new_reward)
        return actual_rewards

    def add_snail_task(self, task):
        input_field = self.browser.find_element(By.NAME, 'new_snail_task_name')
        input_field.send_keys(task.name)
        self.browser.find_element(By.NAME, 'submit_snail_task').click()

    def add_quail_task(self, task):
        input_field = self.browser.find_element(By.NAME, 'new_quail_task_name')
        input_field.send_keys(task.name)
        self.browser.find_element(By.NAME, 'submit_quail_task').click()

    def add_watermelon_task(self, task):
        input_field = self.browser.find_element(By.NAME, 'new_watermelon_task_name')
        input_field.send_keys(task.name)
        self.browser.find_element(By.NAME, 'submit_watermelon_task').click()

    def get_current_watermelons(self):
        watermelons = self.browser.find_elements(By.NAME, 'watermelon_task_name')
        actual_watermelons = []
        for watermelon in watermelons:
            actual_watermelons.append(WatermelonTask(watermelon.text))
        return actual_watermelons

    def get_current_tasks(self):
        snail_tasks = self.browser.find_elements(By.NAME, 'snail_task_name')
        quail_tasks = self.browser.find_elements(By.NAME, 'quail_task_name')
        actual_snail_tasks = []
        actual_quail_tasks = []
        for task in snail_tasks:
            actual_snail_tasks.append(SnailTask(task.text))
        for task in quail_tasks:
            actual_quail_tasks.append(QuailTask(task.text))
        return actual_snail_tasks, actual_quail_tasks

    def complete_task(self):
        self.browser.find_element(By.NAME, 'complete').click()

    def get_bad_ass_points_total(self):
        return int(self.browser.find_element(By.NAME, 'bad_ass_points_total').text)

    def get_validation_error_messages(self):
        error_messages = []
        for error_message in self.browser.find_elements(By.CLASS_NAME, 'wrong'):
            error_messages.append(error_message.text)
        return error_messages

    def get_upper_level_error_messages(self):
        return self.browser.find_element(By.NAME, 'error').text

    def add_reward_with_empty_name(self):
        input_field = self.browser.find_element(By.NAME, 'new_reward_name')
        input_field.send_keys('')
        self.browser.find_element(By.NAME, 'submit_reward').click()

    def add_reward_with_cost(self, cost):
        input_field = self.browser.find_element(By.NAME, 'new_reward_cost')
        input_field.send_keys(cost)
        self.browser.find_element(By.NAME, 'submit_reward').click()

    def purchase_reward(self):
        self.browser.find_element(By.NAME, 'purchase').click()
