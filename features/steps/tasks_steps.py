from model.task import *
from model.bad_ass_points_purse import BadAssPointsPurse
from model.repositories.bad_ass_points_repository import BadAssPointsRepository
from model.repositories.mongo_wrapper import MongoWrapper
from nose import tools


@when(u'I create a snail task called "{task}"')
def step_impl(context, task):
    expenses = SnailTask(task)
    context.expected_snail_tasks.append(expenses)
    context.home_page.add_snail_task(expenses)


@then(u'I should be able to view all tasks')
def step_impl(context):
    actual_snail_tasks, actual_quail_tasks = context.home_page.get_current_tasks()
    for expected_snail in context.expected_snail_tasks:
        assert expected_snail in actual_snail_tasks
    for expected_quail in context.expected_quail_tasks:
        assert expected_quail in actual_quail_tasks


@when(u'I create a quail task called "{task}"')
def step_impl(context, task):
    book = QuailTask(task)
    context.expected_quail_tasks.append(book)
    context.home_page.add_quail_task(book)


@given(u'I create a snail task called "{task}"')
def step_impl(context, task):
    expenses = SnailTask(task)
    context.expected_snail_tasks.append(expenses)
    context.home_page.add_snail_task(expenses)


@when(u'I complete the snail task called "Do expenses for October"')
def step_impl(context):
    context.home_page.complete_task()


@then(u'the snail task "{task}" should be deleted')
def step_impl(context, task):
    actual_snail_tasks, actual_quail_tasks = context.home_page.get_current_tasks()
    unexpected_task = SnailTask(task)
    tools.assert_not_in(unexpected_task, actual_snail_tasks)


@given(u'I create a quail task called "{task}"')
def step_impl(context, task):
    book = QuailTask(task)
    context.expected_quail_tasks.append(book)
    context.home_page.add_quail_task(book)


@when(u'I complete the quail task called "Row 5k"')
def step_impl(context):
    context.home_page.complete_task()


@then(u'the quail task "{task}" should be deleted')
def step_impl(context, task):
    actual_snail_tasks, actual_quail_tasks = context.home_page.get_current_tasks()
    unexpected_task = QuailTask(task)
    tools.assert_not_in(unexpected_task, actual_quail_tasks)


@then(u'I should only see one snail task called "{task}"')
def step_impl(context, task):
    actual_snail_tasks, actual_quail_tasks = context.home_page.get_current_tasks()
    task = SnailTask(task)
    tools.assert_equal(1, actual_snail_tasks.count(task))


@then(u'I should only see one quail task called "{task}"')
def step_impl(context, task):
    actual_snail_tasks, actual_quail_tasks = context.home_page.get_current_tasks()
    task = QuailTask(task)
    tools.assert_equal(1, actual_quail_tasks.count(task))


@given(u'I create a watermelon task called "{task_name}"')
def step_impl(context, task_name):
    task = WatermelonTask(task_name)
    context.home_page.add_watermelon_task(task)


@then(u'I should only see one watermelon task called "{task}"')
def step_impl(context, task):
    actual_watermelon_tasks = context.home_page.get_current_watermelons()
    task = WatermelonTask(task)
    tools.assert_equal(1, actual_watermelon_tasks.count(task))


@when(u'I complete the watermelon task called "Finish the book DNS and BIND"')
def step_impl(context):
    context.home_page.complete_task()
