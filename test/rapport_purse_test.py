import mock
from model.repositories.rapport_repository import RapportRepository
from model.todo_list import TodoList
from model.task import SnailTask
from model.task import QuailTask
from model.rapport_purse import RapportPurse

mock_rapport_storage = mock.create_autospec(RapportRepository)
rapport_purse = RapportPurse(mock_rapport_storage)


def test_rapport_is_incremented_by_one_for_Snail_task():
    rapport_purse.add_rapport_for(SnailTask('omanyte'))

    mock_rapport_storage.increment_rapport_by.assert_called_with(1)


def test_rapport_is_incremented_by_five_for_Quail_task():
    rapport_purse.add_rapport_for(QuailTask('chiquail'))

    mock_rapport_storage.increment_rapport_by.assert_called_with(10)
