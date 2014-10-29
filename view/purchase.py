from home import Home


class PurchaseReward:
    def __init__(self):
        self.home_page = Home()

    def POST(self, name):
        if not complete_task_form.validates():
            return self.home_page.render_home_page()


