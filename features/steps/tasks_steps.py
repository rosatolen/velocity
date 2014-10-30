from model.task import *
from model.bad_ass_points_purse import BadAssPointsPurse
from model.repositories.bad_ass_points_repository import BadAssPointsRepository
from model.repositories.mongo_wrapper import MongoWrapper
from nose import tools


@when(u'I create a snail task called "Do expenses for October"')
def step_impl(context):
    expenses = SnailTask("Do expenses for October")
    context.expected_snail_tasks.append(expenses)
    context.home_page.add_snail_task(expenses)

@then(u'I should be able to view all tasks')
def step_impl(context):
    actual_snail_tasks, actual_quail_tasks = context.home_page.get_current_tasks()
    for expected_snail in context.expected_snail_tasks:
        assert expected_snail in actual_snail_tasks
    for expected_quail in context.expected_quail_tasks:
        assert expected_quail in actual_quail_tasks

@when(u'I create a quail task called "Finish the book DNS and BIND"')
def step_impl(context):
    book = QuailTask("Finish the book DNS and BIND")
    context.expected_quail_tasks.append(book)
    context.home_page.add_quail_task(book)

@given(u'I create a snail task called "Do expenses for October"')
def step_impl(context):
    expenses = SnailTask('Do expenses for October')
    context.expected_snail_tasks.append(expenses)
    context.home_page.add_snail_task(expenses)

@when(u'I complete the snail task called "Do expenses for October"')
def step_impl(context):
    context.home_page.complete_task()

@then(u'the snail task "Do expenses for October" should be deleted')
def step_impl(context):
    actual_snail_tasks, actual_quail_tasks = context.home_page.get_current_tasks()
    unexpected_task = SnailTask('Do expenses for October')
    tools.assert_not_in(unexpected_task, actual_snail_tasks)

@given(u'I create a quail task called "Finish the book DNS and BIND"')
def step_impl(context):
    book = QuailTask("Finish the book DNS and BIND")
    context.expected_quail_tasks.append(book)
    context.home_page.add_quail_task(book)

@given(u'I create a snail task called "Finish the book DNS and BIND"')
def step_impl(context):
    book = SnailTask("Finish the book DNS and BIND")
    context.expected_snail_tasks.append(book)
    context.home_page.add_snail_task(book)

@when(u'I complete the quail task called "Finish the book DNS and BIND"')
def step_impl(context):
    context.home_page.complete_task()

@then(u'the quail task "Finish the book DNS and BIND" should be deleted')
def step_impl(context):
    actual_snail_tasks, actual_quail_tasks = context.home_page.get_current_tasks()
    unexpected_task = QuailTask("Finish the book DNS and BIND")
    tools.assert_not_in(unexpected_task, actual_quail_tasks)

@then(u'I should only see one snail task called "Do expenses for October"')
def step_impl(context):
    actual_snail_tasks, actual_quail_tasks = context.home_page.get_current_tasks()
    task = SnailTask('Do expenses for October')
    tools.assert_equal(1, actual_snail_tasks.count(task))

@then(u'I should only see one quail task called "Finish the book DNS and BIND"')
def step_impl(context):
    actual_snail_tasks, actual_quail_tasks = context.home_page.get_current_tasks()
    task = QuailTask('Finish the book DNS and BIND')
    tools.assert_equal(1, actual_quail_tasks.count(task))

@then(u'I should get an error message that says "Task already exists"')
def step_impl(context):
    error_messages = context.home_page.get_validation_error_messages()
    tools.assert_in('Task already exists', error_messages)
