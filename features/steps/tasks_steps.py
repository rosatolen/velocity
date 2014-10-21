from behave import *
import subprocess
from task import *

@when(u'I create a snail task called "Do expenses for October"')
def step_impl(context):
  expenses = SnailTask("Do expenses for October")
  context.expected_tasks = []
  context.expected_tasks.append(expenses)
  subprocess.call("python task_repository.py add 'Do expenses for October'", shell=True)

@when(u'I create a quail task called "Finish the book DNS and BIND"')
def step_impl(context):
  book = QuailTask("Finish the book DNS and BIND")
  context.expected_tasks.append(book)
  subprocess.call("python task_repository.py add 'Finish the book DNS and BIND'", shell=True)

@then(u'I should be able to view all tasks')
def step_impl(context):
  process = subprocess.Popen(["python task_repository.py viewall"], stdout=subprocess.PIPE, shell=True)
  output = process.communicate()[0].strip()

  for expected_task in context.expected_tasks:
    assert(expected_task.name in output)
