from behave import *
import subprocess

@when(u'I save a reward called "A kiss from my girlfriend" with a price of 100 Tokens')
def step_impl(context):
  context.expected_reward = "A kiss from my girlfriend"
  subprocess.call("python rewards.py 'A kiss from my girlfriend' 100", shell=True)

@then(u'I should be able to list it')
def step_impl(context):
  process = subprocess.Popen(["python view.py rewards"],stdout=subprocess.PIPE, shell=True)
  output = process.communicate()[0].strip()
  assert(context.expected_reward in output)
