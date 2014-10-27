import mock
from nose import tools
from model.repositories.mongo_wrapper import MongoWrapper
from model.repositories.task_repository import TaskRepository
from model.task import SnailTask
from model.task import QuailTask


mock_task_storage = mock.create_autospec(MongoWrapper)
task_repo = TaskRepository(mock_task_storage)


def test_call_to_mongo_when_adding_a_snail_task():
    task = SnailTask('omanyte')

    task_repo.add(task)

    mock_task_storage.insert_task.assert_called_with({'name': task.name, 'size': 'snail'})


def test_call_to_mongo_when_getting_tasks():
    db_tasks = [{'name': 'omanyte', 'size': 'snail'}, {"name": 'chiquail', 'size': 'chiquail'}]
    mock_task_storage.find_tasks.return_value = db_tasks
    expected_tasks = [SnailTask('omanyte'), QuailTask('chiquail')]

    domain_tasks = task_repo.get_tasks()

    tools.assert_list_equal(expected_tasks, domain_tasks)


def test_call_to_mongo_when_adding_a_quail_task():
    task = QuailTask('chiquail')

    task_repo.add(task)

    mock_task_storage.insert_task.assert_called_with({'name': task.name, 'size': 'quail'})


def test_call_to_mongo_for_one_task():
    db_tasks = [{'name': 'omanyte', 'size': 'snail'}, {"name": 'chiquail', 'size': 'chiquail'}]
    mock_task_storage.find_tasks.return_value = db_tasks

    actual_task = task_repo.get_task('chiquail')

    expected_task = QuailTask('chiquail')
    tools.assert_equal(expected_task, actual_task)


def test_call_to_mongo_for_one_task():
    db_tasks = [{'name': 'omanyte', 'size': 'snail'}, {"name": 'chiquail', 'size': 'chiquail'}]
    mock_task_storage.find_tasks.return_value = db_tasks

    actual_task = task_repo.get_task('omanyte')

    expected_task = SnailTask('omanyte')
    tools.assert_equal(expected_task, actual_task)
