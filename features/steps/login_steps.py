from nose import tools
from selenium import webdriver
from selenium.webdriver.common.by import By
from model.reward import Reward
from features.page_navigation import *


@when(u'I try to access the home page')
def step_impl(context):
    home_page.navigate_to_home_page(context)


@then(u'I should be asked to login')
def step_impl(context):
    login_page.assert_that_current_page_is_login_page(context.browser)


@then(u'I should be asked to login in a different browser')
def step_impl(context):
    login_page.assert_that_current_page_is_login_page(context.other_browser)


@given(u'I register as the user "{username}"')
def step_impl(context, username):
    context.username = username
    registration_page.register(context.browser, username, 'password', 'password')


@when(u'I try to login as "{username}"')
def step_impl(context, username):
    login_page.login(context.browser, username, 'password')


@when(u'I try to login as "{username}" with a bad password')
def step_impl(context, username):
    login_page.login(context.browser, username, 'badpassword')


@then(u'I should be able to see my home page')
def step_impl(context):
    home_page.assert_that_current_page_is_home_page(context)


@when(u'I logout')
def step_impl(context):
    context.current_page.click_on_logout_link()


@then(u'I should be able to register')
def step_impl(context):
    context.current_page.click_on_registration_link()


@when(u'I register with a blank username')
def step_impl(context):
    registration_page.register(context.browser, '', 'password', 'password')


@given(u'I navigate to the registration page')
def step_impl(context):
    registration_page.navigate_to_registration_page(context)


@when(u'I leave the username on the login form blank')
def step_impl(context):
    login_page.login(context.browser, '', 'password')


@when(u'I leave the password on the login form blank')
def step_impl(context):
    login_page.login(context.browser, 'Amber', '')


@when(u'I register with mismatching passwords')
def step_impl(context):
    registration_page.register(context.browser, 'username', 'cat', 'dog')


@when(u'I open the home page on a different browser')
def step_impl(context):
    context.other_browser = webdriver.Firefox()
    context.other_browser.get('localhost:1234')


@when(u'I register as the user "{username}" in a different browser')
def step_impl(context, username):
    registration_page.register(context.other_browser, username, 'password', 'password')


@when(u'I try to login as "{username}" in a different browser')
def step_impl(context, username):
    login_page.login(context.other_browser, username, 'password')


@then(u'I should not see the reward "{reward_name}" with a cost {cost} listed in a different browser')
def step_impl(context, reward_name, cost):
    actual_rewards = home_page.get_rewards(context.other_browser)
    tools.assert_not_in(Reward(reward_name, int(cost)), actual_rewards)
    context.other_browser.quit()
