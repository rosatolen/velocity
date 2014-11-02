from nose import tools
from model.reward import *
from test_storage_access import TestStorageAccess
from behave import use_step_matcher, given, when, then
use_step_matcher("parse")

@when(u'I save a reward called "{reward_name}" with a cost of {reward_cost} Bad Ass Points')
def step_impl(context, reward_name, reward_cost):
    kiss = Reward(reward_name, int(reward_cost))
    context.expected_rewards.append(kiss)
    context.current_page.add_reward(kiss)


@then(u'I should be able to view all rewards')
def step_impl(context):
    actual_rewards = context.current_page.get_rewards()
    tools.assert_equal(context.expected_rewards, actual_rewards)


@when(u'I save a reward with an empty name')
def step_impl(context):
    context.current_page.add_reward_with_empty_name()


@then(u'I should get an input error message that says "{expected_error}"')
def step_impl(context, expected_error):
    error_messages = context.current_page.get_validation_error_messages()
    tools.assert_in(expected_error, error_messages)


@given(u'I have a reward called "{reward_name}" with a cost of {reward_cost} Bad Ass Points')
def step_impl(context, reward_name, reward_cost):
    kiss = Reward(reward_name, int(reward_cost))
    context.expected_rewards.append(kiss)
    context.current_page.add_reward(kiss)


@then(u'I should not see the reward "{name}" with a cost {cost} listed')
def step_impl(context, name, cost):
    actual_rewards = context.current_page.get_rewards()
    tools.assert_not_in(Reward(name, int(cost)), actual_rewards)


@given(u'I have {amount} Bad Ass Points')
def step_impl(context, amount):
    TestStorageAccess().set_bad_ass_points(int(amount))


@when(u'I purchase the reward')
def step_impl(context):
    context.current_page.purchase_reward()


@then(u'I should have {amount} Bad Ass Points')
def step_impl(context, amount):
    bad_ass_points_total = context.current_page.get_bad_ass_points_total()
    tools.assert_equal(int(amount), bad_ass_points_total)


@then(u'I should only see one reward called "{reward_name}" with a cost of {cost}')
def step_impl(context, reward_name, cost):
    actual_rewards = context.current_page.get_rewards()
    reward = Reward(reward_name, int(cost))
    tools.assert_equal(1, actual_rewards.count(reward))


@when(u'I add a reward with "blah" as the cost')
def step_impl(context):
    context.current_page.add_reward_with_cost("blah")


@then(u'I should get an upper level error message that says "{message}"')
def step_impl(context, message):
    error_message = context.current_page.get_upper_level_error_messages()
    tools.assert_equal(message, error_message)
