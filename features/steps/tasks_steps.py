from model.task import *
from nose import tools
from features.page_navigation import *


@when(u'I create a snail task called "{task}"')
def step_impl(context, task):
    expenses = SnailTask(task)
    context.expected_snail_tasks.append(expenses)
    home_page.add_snail_task(context, expenses)


@then(u'I should be able to view all tasks')
def step_impl(context):
    actual_snail_tasks, actual_quail_tasks = home_page.get_current_tasks(context)
    for expected_snail in context.expected_snail_tasks:
        assert expected_snail in actual_snail_tasks
    for expected_quail in context.expected_quail_tasks:
        assert expected_quail in actual_quail_tasks


@when(u'I create a quail task called "{task}"')
def step_impl(context, task):
    book = QuailTask(task)
    context.expected_quail_tasks.append(book)
    home_page.add_quail_task(context, book)


@given(u'I create a snail task called "{task}"')
def step_impl(context, task):
    expenses = SnailTask(task)
    context.expected_snail_tasks.append(expenses)
    home_page.add_snail_task(context, expenses)


@when(u'I complete the snail task called "Do expenses for October"')
def step_impl(context):
    home_page.complete_task(context)


@then(u'the snail task "{task}" should be deleted')
def step_impl(context, task):
    actual_snail_tasks, actual_quail_tasks = home_page.get_current_tasks(context)
    unexpected_task = SnailTask(task)
    tools.assert_not_in(unexpected_task, actual_snail_tasks)


@given(u'I create a quail task called "{task}"')
def step_impl(context, task):
    book = QuailTask(task)
    context.expected_quail_tasks.append(book)
    home_page.add_quail_task(context, book)


@when(u'I complete the quail task called "Row 5k"')
def step_impl(context):
    home_page.complete_task(context)


@then(u'the quail task "{task}" should be deleted')
def step_impl(context, task):
    actual_snail_tasks, actual_quail_tasks = home_page.get_current_tasks(context)
    unexpected_task = QuailTask(task)
    tools.assert_not_in(unexpected_task, actual_quail_tasks)


@then(u'I should only see one snail task called "{task}"')
def step_impl(context, task):
    actual_snail_tasks, actual_quail_tasks = home_page.get_current_tasks(context)
    task = SnailTask(task)
    tools.assert_equal(1, actual_snail_tasks.count(task))


@then(u'I should only see one quail task called "{task}"')
def step_impl(context, task):
    actual_snail_tasks, actual_quail_tasks = home_page.get_current_tasks(context)
    task = QuailTask(task)
    tools.assert_equal(1, actual_quail_tasks.count(task))


@given(u'I create a watermelon task called "{task_name}"')
def step_impl(context, task_name):
    task = WatermelonTask(task_name)
    home_page.add_watermelon_task(context, task)


@then(u'I should only see one watermelon task called "{task}"')
def step_impl(context, task):
    actual_watermelon_tasks = home_page.get_current_watermelons(context)
    task = WatermelonTask(task)
    tools.assert_equal(1, actual_watermelon_tasks.count(task))


@when(u'I complete the watermelon task called "Finish the book DNS and BIND"')
def step_impl(context):
    home_page.complete_task(context)


@when(u'I delete the task')
def step_impl(context):
    context.current_page.delete_task()


@then(u'I should not see any tasks')
def step_impl(context):
    actual_snail_tasks, actual_quail_tasks = home_page.get_current_tasks(context)
    actual_watermelon_tasks = home_page.get_current_watermelons(context)
    tools.assert_equal([], actual_snail_tasks)
    tools.assert_equal([], actual_quail_tasks)
    tools.assert_equal([], actual_watermelon_tasks)


@when(u'I create a "{theme}" themed snail task called "{task_name}"')
def step_impl(context, theme, task_name):
    home_page.add_snail_task(theme, task_name)

@then(u'I should be able to view all tasks with their themes')
def step_impl(context):
    assert False
