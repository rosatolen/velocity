from behave import *
from nose import tools
from model.bad_ass_points_purse import BadAssPointsPurse
from model.repositories.bad_ass_points_repository import BadAssPointsRepository
from model.repositories.mongo_wrapper import MongoWrapper

@then(u'I should have 1 more bad ass point in my bad ass points purse')
def step_impl(context):
    bad_ass_points_purse = BadAssPointsPurse(BadAssPointsRepository(MongoWrapper()))
    tools.assert_equal(1, bad_ass_points_purse.total)

@then(u'I should have 10 more bad ass points in my bad ass points purse')
def step_impl(context):
    bad_ass_points_purse = BadAssPointsPurse(BadAssPointsRepository(MongoWrapper()))
    tools.assert_equal(11, bad_ass_points_purse.total)

@then(u'I should see my bad ass points increase to 10')
def step_impl(context):
    bad_ass_points_total = context.home_page.get_bad_ass_points_total()
    tools.assert_equal(10, bad_ass_points_total)
