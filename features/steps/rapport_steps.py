from behave import *
from nose import tools

@then(u'I should see my rapport increase to 10')
def step_impl(context):
    rapport_total = context.home_page.get_rapport_total()
    tools.assert_equal(10, rapport_total)
