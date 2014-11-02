# DEBT refactor these imports into the environment
from behave import when, then, use_step_matcher
from model.repositories.user_repository import UserRepository
from model.repositories.mongo_wrapper import MongoWrapper

use_step_matcher("parse")


@when(u'I try to access the home page')
def step_impl(context):
    context.current_page.navigate_to_home_page()


@then(u'I should be asked to login')
def step_impl(context):
    context.current_page.assert_that_current_page_is_login_page()


@given(u'I register as the user "{username}"')
def step_impl(context, username):
    context.current_page.navigate_to_registration_page()
    context.current_page.register(username)


@when(u'I try to login as "{username}"')
def step_impl(context, username):
    context.current_page.login(username)


@then(u'I should be able to see my home page')
def step_impl(context):
    context.current_page.assert_that_current_page_is_home_page()


@when(u'I logout')
def step_impl(context):
    context.current_page.logout()
