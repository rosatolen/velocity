from nose import tools
from selenium import webdriver
from selenium.webdriver.common.by import By
from model.reward import Reward


@when(u'I try to access the home page')
def step_impl(context):
    context.current_page.navigate_to_home_page()


@then(u'I should be asked to login')
def step_impl(context):
    context.current_page.assert_that_current_page_is_login_page()


@then(u'I should be asked to login in a different browser')
def step_impl(context):
    current_page_name = context.other_browser.find_element(By.NAME, 'page_name').text
    tools.assert_equal('Login', current_page_name)


@given(u'I register as the user "{username}"')
def step_impl(context, username):
    context.username = username
    context.current_page.navigate_to_registration_page()
    context.current_page.register(username, 'password', 'password')


@when(u'I try to login as "{username}"')
def step_impl(context, username):
    context.current_page.login(username, 'password')


@when(u'I try to login as "{username}" with a bad password')
def step_impl(context, username):
    context.current_page.login(username, 'badpassword')


@then(u'I should be able to see my home page')
def step_impl(context):
    context.current_page.assert_that_current_page_is_home_page()


@when(u'I logout')
def step_impl(context):
    context.current_page.click_on_logout_link()


@then(u'I should be able to register')
def step_impl(context):
    context.current_page.click_on_registration_link()


@when(u'I register with a blank username')
def step_impl(context):
    context.current_page.register('', 'password', 'password')


@given(u'I navigate to the registration page')
def step_impl(context):
    context.current_page.navigate_to_registration_page()


@when(u'I leave the username on the login form blank')
def step_impl(context):
    context.current_page.login('', 'password')


@when(u'I leave the password on the login form blank')
def step_impl(context):
    context.current_page.login('Amber', '')


@when(u'I register with mismatching passwords')
def step_impl(context):
    context.current_page.register('username', 'cat', 'dog')


@when(u'I open the home page on a different browser')
def step_impl(context):
    context.other_browser = webdriver.Firefox()
    context.other_browser.get('localhost:1234')


@when(u'I register as the user "{username}" in a different browser')
def step_impl(context, username):
    context.other_browser.get('localhost:1234/register')
    input_field = context.other_browser.find_element(By.NAME, 'username')
    input_field.send_keys(username)
    input_field = context.other_browser.find_element(By.NAME, 'password')
    input_field.send_keys('password')
    input_field = context.other_browser.find_element(By.NAME, 'retype_password')
    input_field.send_keys('password')
    context.other_browser.find_element(By.NAME, 'register').click()


@when(u'I try to login as "{username}" in a different browser')
def step_impl(context, username):
    input_field = context.other_browser.find_element(By.NAME, 'username')
    input_field.send_keys(username)
    input_field = context.other_browser.find_element(By.NAME, 'password')
    input_field.send_keys('password')
    context.other_browser.find_element(By.NAME, 'login').click()


@then(u'I should not see the reward "{reward_name}" with a cost {cost} listed in a different browser')
def step_impl(context, reward_name, cost):
    rewards = context.other_browser.find_elements(By.NAME, 'reward')
    costs = context.other_browser.find_elements(By.NAME, 'cost')
    actual_rewards = []
    for reward, cost in zip(rewards, costs):
        new_reward = Reward(reward.text, int(cost.text))
        actual_rewards.append(new_reward)

    tools.assert_not_in(Reward(reward_name, int(cost)), actual_rewards)
    context.other_browser.quit()
