from nose import tools
from model.repositories.user_repository import UserRepository
from model.repositories.mongo_wrapper import MongoWrapper



@when(u'I try to access the home page')
def step_impl(context):
    context.current_page.navigate_to_home_page()


@then(u'I should be asked to login')
def step_impl(context):
    context.current_page.assert_that_current_page_is_login_page()


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


@given(u'I reset my user')
def step_impl(context):
    context.browser.get('localhost:1234/logout')
    context.browser.get('localhost:1234')


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
