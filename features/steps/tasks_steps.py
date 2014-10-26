from behave import *
import subprocess
from task import *

@when(u'I create a snail task called "Do expenses for October"')
def step_impl(context):
  expenses = SnailTask("Do expenses for October")
  context.expected_tasks = []
  context.expected_tasks.append(expenses)
  context.home_page.add_task(expenses)

@when(u'I create a quail task called "Finish the book DNS and BIND"')
def step_impl(context):
  book = QuailTask("Finish the book DNS and BIND")
  context.expected_tasks.append(book)
  context.home_page.add_task(expenses)

@then(u'I should be able to view all tasks')
def step_impl(context):
  actual_tasks = context.home_page.get_current_tasks()
  for expected_task in context.expected_tasks:
    assert expected_task in actual_tasks
