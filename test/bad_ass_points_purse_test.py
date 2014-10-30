import mock
from model.repositories.bad_ass_points_repository import BadAssPointsRepository
from model.todo_list import TodoList
from model.task import SnailTask
from model.task import QuailTask
from model.bad_ass_points_purse import BadAssPointsPurse

mock_bad_ass_points_storage = mock.create_autospec(BadAssPointsRepository)
bad_ass_points_purse = BadAssPointsPurse(mock_bad_ass_points_storage)


def test_bad_ass_points_are_incremented_by_one_for_Snail_task():
    bad_ass_points_purse.add_bad_ass_points_for(SnailTask('omanyte'))

    mock_bad_ass_points_storage.increment_bad_ass_points_by.assert_called_with(1)


def test_bad_ass_points_are_incremented_by_ten_for_Quail_task():
    bad_ass_points_purse.add_bad_ass_points_for(QuailTask('chiquail'))

    mock_bad_ass_points_storage.increment_bad_ass_points_by.assert_called_with(8)


def test_subtracting_reward_cost_for_purchase():
    bad_ass_points_purse.subtract_reward_cost(1)

    mock_bad_ass_points_storage.decrement_bad_ass_points_by.assert_called_with(1)
