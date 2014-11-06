@when(u'I pause for {number} seconds')
def step_impl(context, number):
    import time
    time.sleep(int(number))
