from nose import tools
from features.page_navigation import *


@then(u'I should have {amount} more bad ass points in my bad ass points purse')
def step_impl(context, amount):
    total = home_page.get_bad_ass_points_total(context)
    tools.assert_equal(int(amount), total)

@then(u'I should see my bad ass points increase to {amount}')
def step_impl(context, amount):
    total = home_page.get_bad_ass_points_total(context)
    tools.assert_equal(int(amount), total)
