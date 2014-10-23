import subprocess
from behave import *
from reward import *
from features.page_navigation import *

@when(u'I save a reward called "A kiss from my girlfriend" with a cost of 100 Tokens')
def step_impl(context):
  kiss = Reward("A kiss from my girlfriend", 100)
  context.expected_rewards = []
  context.expected_rewards.append(kiss)
  context.home_page.add_reward(kiss)

@when(u'I save a reward called "Go to London" with a cost of 2000 Tokens')
def step_impl(context):
  london = Reward("Go to London", 2000)
  context.expected_rewards.append(london)
  context.home_page.add_reward(london)

@then(u'I should be able to view all rewards')
def step_impl(context):
  process = subprocess.Popen(["python reward_repository.py viewall"], stdout=subprocess.PIPE, shell=True)
  output = process.communicate()[0].strip()

  for expected_reward in context.expected_rewards:
    assert(expected_reward.name in output)
    assert(str(expected_reward.cost) in output)
