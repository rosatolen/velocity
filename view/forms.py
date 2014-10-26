import web


class RewardForm:
    def __init__(self):
        self.form = web.form.Form(
            web.form.Textbox('new_reward_name', web.form.notnull, description=""),
            web.form.Textbox('new_reward_cost', web.form.notnull, description=""),
            web.form.Button('submit_reward', html='Add Reward'),
        )


class SnailTaskForm:
    def __init__(self):
        self.form = web.form.Form(
            web.form.Textbox('new_snail_task_name', web.form.notnull, description=""),
            web.form.Button('submit_snail_task', html='Add Snail Task'),
        )


class QuailTaskForm:
    def __init__(self):
        self.form = web.form.Form(
            web.form.Textbox('new_quail_task_name', web.form.notnull, description=""),
            web.form.Button('submit_quail_task', html='Add Quail Task'),
        )
