from nose import tools
from selenium.webdriver.common.by import By
from model.reward import Reward
from model.task import *


def navigate_to_home_page(context):
    context.browser.get('localhost:1234')


def assert_that_current_page_is_home_page(context):
    bad_ass_points = context.browser.find_element(By.NAME, 'bad_ass_points').text
    tools.assert_true('Bad Ass Points Total:' in bad_ass_points)


def get_rewards(browser):
    rewards = browser.find_elements(By.NAME, 'reward')
    costs = browser.find_elements(By.NAME, 'cost')

    actual_rewards = []
    for reward, cost in zip(rewards, costs):
        new_reward = Reward(reward.text, int(cost.text))
        actual_rewards.append(new_reward)

    return actual_rewards


def add_reward(context, reward):
    input_field = context.browser.find_element(By.NAME, 'new_reward_name')
    input_field.send_keys(reward.name)
    input_field = context.browser.find_element(By.NAME, 'new_reward_cost')
    input_field.send_keys(reward.cost)
    context.browser.find_element(By.NAME, 'submit_reward').click()


def add_reward_with_empty_name(context):
    input_field = context.browser.find_element(By.NAME, 'new_reward_name')
    input_field.send_keys('')
    context.browser.find_element(By.NAME, 'submit_reward').click()


def get_bad_ass_points_total(context):
    return int(context.browser.find_element(By.NAME, 'bad_ass_points_total').text)


def purchase_reward(context):
    context.browser.find_element(By.NAME, 'purchase').click()


def add_reward_with_cost(context, cost):
    input_field = context.browser.find_element(By.NAME, 'new_reward_cost')
    input_field.send_keys(cost)
    context.browser.find_element(By.NAME, 'submit_reward').click()


def delete_reward(context):
    context.browser.find_element(By.NAME, 'delete_reward').click()


def add_snail_task(context, task):
    input_field = context.browser.find_element(By.NAME, 'new_snail_task_name')
    input_field.send_keys(task.name)
    context.browser.find_element(By.NAME, 'submit_snail_task').click()


def complete_task(context):
    context.browser.find_element(By.NAME, 'complete').click()


def get_current_tasks(context):
    snail_tasks = context.browser.find_elements(By.NAME, 'snail_task_name')
    quail_tasks = context.browser.find_elements(By.NAME, 'quail_task_name')
    actual_snail_tasks = []
    actual_quail_tasks = []
    for task in snail_tasks:
        actual_snail_tasks.append(SnailTask(task.text))
    for task in quail_tasks:
        actual_quail_tasks.append(QuailTask(task.text))
    return actual_snail_tasks, actual_quail_tasks


def add_quail_task(context, task):
    input_field = context.browser.find_element(By.NAME, 'new_quail_task_name')
    input_field.send_keys(task.name)
    context.browser.find_element(By.NAME, 'submit_quail_task').click()


def add_watermelon_task(context, task):
    input_field = context.browser.find_element(By.NAME, 'new_watermelon_task_name')
    input_field.send_keys(task.name)
    context.browser.find_element(By.NAME, 'submit_watermelon_task').click()


def get_current_watermelons(context):
    watermelons = context.browser.find_elements(By.NAME, 'watermelon_task_name')
    actual_watermelons = []
    for watermelon in watermelons:
        actual_watermelons.append(WatermelonTask(watermelon.text))
    return actual_watermelons


def get_todays_bad_ass_points(context):
    return int(context.browser.find_element(By.NAME, 'todays_points').text)
