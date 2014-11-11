import mock
from datetime import date, datetime, timedelta
from nose import tools
from model.purse import Purse
from pytz import timezone

pacific = timezone('US/Pacific')


def test_increment_todays_points():
    purse = Purse(1, 1, date.today(), pacific)

    purse.add(8)

    tools.assert_equal(9, purse.todays_total)
    tools.assert_equal(9, purse.total)


def test_get_todays_total_when_last_updated_day_was_yesterday():
    today = date.today()
    yesterday = today - timedelta(days=1)
    purse = Purse(2, 2, yesterday, pacific)

    tools.assert_equal(0, purse.todays_total)


def test_ability_to_keep_track_of_todays_points_when_holding_yeseterdays_points():
    today = date.today()
    yesterday = today - timedelta(days=1)
    purse = Purse(2, 2, yesterday, pacific)

    purse.add(12)

    tools.assert_equal(12, purse.todays_total)
    tools.assert_equal(14, purse.total)
    tools.assert_equal(today, purse.last_updated_day)


def test_ability_to_subtract_points():
    purse = Purse(10, 1, date.today(), pacific)

    purse.subtract(5)

    tools.assert_equal(5, purse.total)
    tools.assert_equal(1, purse.todays_total)


def test_string_evaluation_at_creation():
    purse = Purse('0', '0', date.today(), pacific)

    tools.assert_equal(Purse(0, 0, date.today(), pacific), purse)


def test_setting_localize_time_to_us_pacific():
    today = date.today()
    yesterday = today - timedelta(days=1)
    purse = Purse(2, 2, yesterday, pacific)

    purse.add(12)

    tools.assert_equal(12, purse.todays_total)
    tools.assert_equal(14, purse.total)
    tools.assert_equal(today, purse.last_updated_day)
