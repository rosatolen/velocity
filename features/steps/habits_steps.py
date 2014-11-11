from nose import tools
from features.page_navigation import *

@given(u'I create a habit called "{habit_name}" with no theme')
def step_impl(context, habit_name):
    home_page.create_habit(context, habit_name)

@when(u'I complete the habit')
def step_impl(context):
    home_page.complete_habit(context)
