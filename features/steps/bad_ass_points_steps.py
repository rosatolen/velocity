from nose import tools
from model.bad_ass_points_purse import BadAssPointsPurse
from model.repositories.bad_ass_points_repository import BadAssPointsRepository
from model.repositories.mongo_wrapper import MongoWrapper

@then(u'I should have {amount} more bad ass points in my bad ass points purse')
def step_impl(context, amount):
    bad_ass_points_purse = BadAssPointsPurse(BadAssPointsRepository(MongoWrapper()))
    tools.assert_equal(int(amount), bad_ass_points_purse.total)

@then(u'I should see my bad ass points increase to {amount}')
def step_impl(context, amount):
    bad_ass_points_total = context.current_page.get_bad_ass_points_total()
    tools.assert_equal(int(amount), bad_ass_points_total)
