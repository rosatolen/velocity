import mock
from model.repositories.mongo_wrapper import MongoWrapper
from model.todo_list import TodoList
from model.task import SnailTask
from model.rapport_purse import RapportPurse


def test_rapport_is_saved_to_storage():
    mock_rapport_storage = mock.create_autospec(MongoWrapper)
    rapport_purse = RapportPurse(mock_rapport_storage)

    rapport_purse.add_rapport_for(SnailTask('omanyte'))

    mock_rapport_storage.increment_rapport_by.assert_called_with(1)
