from nose import tools
from model.reward import *
from model.user import User
from model.user_repository import UserRepository, MongoWrapper
from features.page_navigation import *


@when(u'I save a reward called "{reward_name}" with a cost of {reward_cost} Bad Ass Points')
def step_impl(context, reward_name, reward_cost):
    kiss = Reward(reward_name, int(reward_cost))
    context.expected_rewards.append(kiss)
    home_page.add_reward(context, kiss)


@then(u'I should be able to view all rewards')
def step_impl(context):
    actual_rewards = home_page.get_rewards(context.browser)
    tools.assert_equal(context.expected_rewards, actual_rewards)


@when(u'I save a reward with an empty name')
def step_impl(context):
    home_page.add_reward_with_empty_name(context)


@then(u'I should get an input error message that says "{expected_error}"')
def step_impl(context, expected_error):
    error_messages = context.current_page.get_validation_error_messages()
    tools.assert_in(expected_error, error_messages)


@given(u'I have a reward called "{reward_name}" with a cost of {reward_cost} Bad Ass Points')
def step_impl(context, reward_name, reward_cost):
    kiss = Reward(reward_name, int(reward_cost))
    context.expected_rewards.append(kiss)
    home_page.add_reward(context, kiss)


@then(u'I should not see the reward "{name}" with a cost {cost} listed')
def step_impl(context, name, cost):
    actual_rewards = home_page.get_rewards(context.browser)
    tools.assert_not_in(Reward(name, int(cost)), actual_rewards)


@given(u'"{username}" has {amount} Bad Ass Points')
def step_impl(context, username, amount):
    user = User(username, [], [], amount)
    user_repository = UserRepository(MongoWrapper())
    user_repository.save_state(user)


@when(u'I purchase the reward')
def step_impl(context):
    home_page.purchase_reward(context)


@then(u'I should have {amount} Bad Ass Points')
def step_impl(context, amount):
    bad_ass_points_total = home_page.get_bad_ass_points_total(context)
    tools.assert_equal(int(amount), bad_ass_points_total)


@then(u'I should only see one reward called "{reward_name}" with a cost of {cost}')
def step_impl(context, reward_name, cost):
    actual_rewards = home_page.get_rewards(context.browser)
    reward = Reward(reward_name, int(cost))
    tools.assert_equal(1, actual_rewards.count(reward))


@when(u'I add a reward with "blah" as the cost')
def step_impl(context):
    home_page.add_reward_with_cost(context, "blah")


@then(u'I should get an upper level error message that says "{message}"')
def step_impl(context, message):
    error_message = context.current_page.get_upper_level_error_messages()
    tools.assert_equal(message, error_message)


@when(u'I delete the reward')
def step_impl(context):
    home_page.delete_reward(context)


@then(u'I should not be able to see any rewards')
def step_impl(context):
    actual_rewards = home_page.get_rewards(context.browser)
    tools.assert_equal([], actual_rewards)
