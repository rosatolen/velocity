import mock
from model.repositories.task_repository import TaskRepository
from model.todo_list import TodoList
from model.task import SnailTask
from model.task import QuailTask
from model.bad_ass_points_purse import BadAssPointsPurse


mock_task_storage = mock.create_autospec(TaskRepository)
mock_bad_ass_points_purse = mock.create_autospec(BadAssPointsPurse)
todo_list = TodoList(mock_task_storage, mock_bad_ass_points_purse)


def test_call_to_mongo_when_deleting_task():
    task_name = 'omanyte'
    mock_task_storage.get_task.return_value = SnailTask(task_name)

    todo_list.complete(task_name)

    mock_task_storage.delete_task.assert_called_with(task_name)


def test_adding_bad_ass_points_to_bad_ass_points_purse():
    task_name = 'omanyte'
    mock_task_storage.get_task.return_value = SnailTask(task_name)

    todo_list.complete(task_name)

    mock_bad_ass_points_purse.add_bad_ass_points_for.assert_called_with(SnailTask(task_name))


def test_adding_bad_ass_points_to_bad_ass_points_purse():
    task_name = 'chiquail'
    mock_task_storage.get_task.return_value = QuailTask(task_name)

    todo_list.complete(task_name)

    mock_bad_ass_points_purse.add_bad_ass_points_for.assert_called_with(QuailTask(task_name))
