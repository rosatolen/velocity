from behave import *
import subprocess

@when(u'I save a reward called "A kiss from my girlfriend" with a price of 100 Tokens')
def step_impl(context):
  context.expected_reward = "A kiss from my girlfriend"
  context.expected_reward_cost = "100"

  subprocess.call("python rewards_repository.py add 'A kiss from my girlfriend' 100", shell=True)

@then(u'I should be able to list it')
def step_impl(context):
  process = subprocess.Popen(["python reward_repository.py viewall"], stdout=subprocess.PIPE, shell=True)
  output = process.communicate()[0].strip()

  assert(context.expected_reward in output)
  assert(context.expected_reward_cost in output)
