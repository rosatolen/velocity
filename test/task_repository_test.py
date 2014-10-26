import mock
from model.mongo_wrapper import MongoWrapper
from model.task_repository import TaskRepository
from model.task import SnailTask


mock_task_storage = mock.create_autospec(MongoWrapper)
task_repo = TaskRepository(mock_task_storage)


def test_call_to_mongo_when_adding_a_snail_task():
    task = SnailTask('chiquail')
    task_repo.add(task)

    mock_task_storage.insert_task.assert_called_with({"name": task.name, "size": "snail"})


def test_call_to_mongo_when_getting_tasks():
    task_repo.get_tasks()

    mock_task_storage.find_tasks().assert_called()
