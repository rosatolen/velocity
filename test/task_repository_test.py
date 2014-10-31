import mock
from nose import tools
from model.repositories.mongo_wrapper import MongoWrapper
from model.repositories.task_repository import TaskRepository
from model.task import SnailTask, QuailTask, WatermelonTask


mock_task_storage = mock.create_autospec(MongoWrapper)
task_repo = TaskRepository(mock_task_storage)


def test_call_to_task_storage_when_adding_a_snail_task():
    task = SnailTask('omanyte')

    task_repo.add(task)

    mock_task_storage.insert_task.assert_called_with({'name': task.name, 'size': 'snail'})


def test_call_to_task_storage_when_getting_tasks():
    db_tasks = [{'name': 'omanyte', 'size': 'snail'}, {"name": 'chiquail', 'size': 'quail'}]
    mock_task_storage.find_tasks.return_value = db_tasks
    expected_tasks = [SnailTask('omanyte'), QuailTask('chiquail')]

    domain_tasks = task_repo.get_tasks()

    tools.assert_list_equal(expected_tasks, domain_tasks)


def test_call_to_task_storage_when_adding_a_quail_task():
    task = QuailTask('chiquail')

    task_repo.add(task)

    mock_task_storage.insert_task.assert_called_with({'name': task.name, 'size': 'quail'})


def test_call_to_task_storage_for_one_quail_task():
    db_tasks = [{'name': 'omanyte', 'size': 'snail'}, {"name": 'chiquail', 'size': 'quail'}]
    mock_task_storage.find_tasks.return_value = db_tasks

    actual_task = task_repo.get_task('chiquail')

    expected_task = QuailTask('chiquail')
    tools.assert_equal(expected_task, actual_task)


def test_call_to_task_storage_for_a_watermelon_task():
    db_tasks = [{'name': 'omanyte', 'size': 'snail'},
                {"name": 'chiquail', 'size': 'quail'},
                {'name': 'nomnom', 'size': 'watermelon'}]
    mock_task_storage.find_tasks.return_value = db_tasks

    actual_task = task_repo.get_task('nomnom')

    expected_task = WatermelonTask('nomnom')
    tools.assert_equal(expected_task, actual_task)


def test_call_to_task_storage_for_one_snail_task():
    db_tasks = [{'name': 'omanyte', 'size': 'snail'}, {"name": 'chiquail', 'size': 'quail'}]
    mock_task_storage.find_tasks.return_value = db_tasks

    actual_task = task_repo.get_task('omanyte')

    expected_task = SnailTask('omanyte')
    tools.assert_equal(expected_task, actual_task)


def test_call_to_task_storage_for_non_existing_task():
    db_tasks = [{'name': 'omanyte', 'size': 'snail'}, {"name": 'chiquail', 'size': 'quail'}]
    mock_task_storage.find_tasks.return_value = db_tasks
    task_name = 'create presentation'

    tools.assert_false(task_repo.contains(task_name))


def test_call_to_task_storage_for_existing_task():
    db_tasks = [{'name': 'omanyte', 'size': 'snail'}, {"name": 'chiquail', 'size': 'quail'}]
    mock_task_storage.find_tasks.return_value = db_tasks
    task_name = 'omanyte'

    tools.assert_true(task_repo.contains(task_name))


def test_call_to_task_storage_for_watermelon_task():
    db_tasks = [{'name': 'omanyte', 'size': 'snail'},
                {"name": 'chiquail', 'size': 'quail'},
                {'name': 'nomnom', 'size': 'watermelon'}]
    mock_task_storage.find_tasks.return_value = db_tasks
    expected_tasks = [SnailTask('omanyte'), QuailTask('chiquail'), WatermelonTask('nomnom')]

    actual_tasks = task_repo.get_tasks()

    tools.assert_equal(expected_tasks, actual_tasks)


def test_add_watermelon_task():
    task = WatermelonTask('omanyte')

    task_repo.add(task)

    mock_task_storage.insert_task.assert_called_with({'name': task.name, 'size': 'watermelon'})
