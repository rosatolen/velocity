from model.reward import *


@when(u'I save a reward called "A kiss from my girlfriend" with a cost of 100 Tokens')
def step_impl(context):
    kiss = Reward("A kiss from my girlfriend", 100)
    context.expected_rewards.append(kiss)
    context.home_page.add_reward(kiss)


@when(u'I save a reward called "Go to London" with a cost of 2000 Tokens')
def step_impl(context):
    london = Reward("Go to London", 2000)
    context.expected_rewards.append(london)
    context.home_page.add_reward(london)


@then(u'I should be able to view all rewards')
def step_impl(context):
    actual_rewards = context.home_page.get_current_rewards()
    for expected_reward in context.expected_rewards:
        assert (actual_rewards.has_key(expected_reward.name))
        assert (actual_rewards[expected_reward.name] == expected_reward.cost)
