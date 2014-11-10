import datetime
from nose import tools
from model.purse import Purse


def test_increment_todays_points():
    purse = Purse(1, 1, datetime.date.today())

    purse.add(8)

    tools.assert_equal(9, purse.todays_total)
    tools.assert_equal(9, purse.total)


def test_get_todays_total_when_last_updated_day_was_yesterday():
    today = datetime.date.today()
    yesterday = today - datetime.timedelta(days=1)
    purse = Purse(2, 2, yesterday)

    tools.assert_equal(0, purse.todays_total)


def test_ability_to_keep_track_of_todays_points_when_holding_yeseterdays_points():
    today = datetime.date.today()
    yesterday = today - datetime.timedelta(days=1)
    purse = Purse(2, 2, yesterday)

    purse.add(12)

    tools.assert_equal(12, purse.todays_total)
    tools.assert_equal(14, purse.total)
    tools.assert_equal(today, purse.last_updated_day)


def test_ability_to_subtract_points():
    purse = Purse(10, 1, datetime.date.today())

    purse.subtract(5)

    tools.assert_equal(5, purse.total)
    tools.assert_equal(1, purse.todays_total)


def test_string_evaluation_at_creation():
    purse = Purse('0', '0', datetime.date.today())

    tools.assert_equal(Purse(0, 0, datetime.date.today()), purse)
