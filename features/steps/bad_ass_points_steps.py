from nose import tools


@then(u'I should have {amount} more bad ass points in my bad ass points purse')
def step_impl(context, amount):
    total = context.current_page.get_bad_ass_points_total()
    tools.assert_equal(int(amount), total)

@then(u'I should see my bad ass points increase to {amount}')
def step_impl(context, amount):
    total = context.current_page.get_bad_ass_points_total()
    tools.assert_equal(int(amount), total)
