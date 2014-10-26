import mock
from nose import tools
from model.mongo_wrapper import MongoWrapper
from model.todo_list import TodoList
from model.task import SnailTask
from model.task import QuailTask


mock_task_storage = mock.create_autospec(MongoWrapper)
todo_list = TodoList(mock_task_storage)


def test_call_to_mongo_when_deleting_task():
    task_name = 'omanyte'
    todo_list.complete(task_name)

    mock_task_storage.delete_task.assert_called_with({'name': task_name})
