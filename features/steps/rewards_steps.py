from nose import tools
from model.reward import *
from test_storage_access import TestStorageAccess


@when(u'I save a reward called "A kiss from my girlfriend" with a cost of 100 Bad Ass Points')
def step_impl(context):
    kiss = Reward("A kiss from my girlfriend", 100)
    context.expected_rewards.append(kiss)
    context.home_page.add_reward(kiss)


@when(u'I save a reward called "Go to London" with a cost of 2000 Bad Ass Points')
def step_impl(context):
    london = Reward("Go to London", 2000)
    context.expected_rewards.append(london)
    context.home_page.add_reward(london)


@then(u'I should be able to view all rewards')
def step_impl(context):
    actual_rewards = context.home_page.get_rewards()
    tools.assert_equal(context.expected_rewards, actual_rewards)


@when(u'I save a reward with an empty name')
def step_impl(context):
    context.home_page.add_reward_with_empty_name()


@then(u'I should get an error message that says "Required"')
def step_impl(context):
    error_messages = context.home_page.get_error_messages()
    tools.assert_in('Required', error_messages)


@given(u'I have a reward called "A kiss from my girlfriend" with a cost of 100 Bad Ass Points')
def step_impl(context):
    kiss = Reward("A kiss from my girlfriend", 100)
    context.expected_rewards.append(kiss)
    context.home_page.add_reward(kiss)


@then(u'I should not see the reward "A kiss from my girlfriend" listed')
def step_impl(context):
    actual_rewards = context.home_page.get_rewards()
    tools.assert_not_in(context.expected_rewards.pop(), actual_rewards)


@given(u'I have 100 Bad Ass Points')
def step_impl(context):
    TestStorageAccess().set_bad_ass_points(100)


@when(u'I purchase the reward')
def step_impl(context):
    context.home_page.purchase_reward()


@then(u'I should have 0 Bad Ass Points')
def step_impl(context):
    bad_ass_points_total = context.home_page.get_bad_ass_points_total()
    tools.assert_equal(0, bad_ass_points_total)


@then(u'I should only see one reward called "A kiss from my girlfriend"')
def step_impl(context):
    actual_rewards = context.home_page.get_rewards()
    reward = Reward('A kiss from my girlfriend', 100)
    tools.assert_equal(1, actual_rewards.count(reward))


@then(u'I should get an error message that says "Reward already exists"')
def step_impl(context):
    error_messages = context.home_page.get_error_messages()
    tools.assert_in('Reward already exists', error_messages)


@when(u'I add a reward with "blah" as the cost')
def step_impl(context):
    context.home_page.add_reward_with_cost("blah")


@then(u'I should get an error message that says "Must be an integer"')
def step_impl(context):
    error_messages = context.home_page.get_error_messages()
    tools.assert_in('Must be an integer', error_messages)
