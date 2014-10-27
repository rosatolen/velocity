import mock
from model.repositories.mongo_wrapper import MongoWrapper
from model.todo_list import TodoList
from model.task import SnailTask
from model.rapport_purse import RapportPurse


mock_task_storage = mock.create_autospec(MongoWrapper)
mock_rapport_purse = mock.create_autospec(RapportPurse)
todo_list = TodoList(mock_task_storage, mock_rapport_purse)


def test_call_to_mongo_when_deleting_task():
    task_name = 'omanyte'
    todo_list.complete(task_name)

    mock_task_storage.delete_task.assert_called_with({'name': task_name})


def test_adding_rapport_to_rapport_purse():
    task_name = 'omanyte'
    todo_list.complete(task_name)

    mock_rapport_purse.add_rapport_for.assert_called_with(SnailTask(task_name))
