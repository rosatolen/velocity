from model.task import *


@when(u'I create a snail task called "Do expenses for October"')
def step_impl(context):
    expenses = SnailTask("Do expenses for October")
    context.expected_snail_tasks = []
    context.expected_snail_tasks.append(expenses)
    context.home_page.add_snail_task(expenses)


@when(u'I create a quail task called "Finish the book DNS and BIND"')
def step_impl(context):
    book = QuailTask("Finish the book DNS and BIND")
    context.expected_quail_tasks = []
    context.expected_quail_tasks.append(book)
    context.home_page.add_quail_task(book)


@then(u'I should be able to view all tasks')
def step_impl(context):
    actual_snail_tasks, actual_quail_tasks = context.home_page.get_current_tasks()
    print 'a ' + str(actual_snail_tasks)
    print 'a ' + str(actual_quail_tasks)
    for expected_snail in context.expected_snail_tasks:
        print 'e ' + str(expected_snail)
        assert expected_snail in actual_snail_tasks
    for expected_quail in context.expected_quail_tasks:
        print 'e ' + str(expected_quail)
        assert expected_quail in actual_quail_tasks
