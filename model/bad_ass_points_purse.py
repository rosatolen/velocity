from task import SnailTask, QuailTask


class BadAssPointsPurse:
    def __init__(self, bad_ass_points_storage):
        self.bad_ass_points_storage = bad_ass_points_storage
        self.total = self.bad_ass_points_storage.get_bad_ass_points_total()
        if self.total is None:
            self.bad_ass_points_storage.initialize_bad_ass_points()
            self.total = 0

    def add_bad_ass_points_for(self, task):
        if isinstance(task, SnailTask):
            self.bad_ass_points_storage.increment_bad_ass_points_by(1)
        elif isinstance(task, QuailTask):
            self.bad_ass_points_storage.increment_bad_ass_points_by(8)
        else:
            self.bad_ass_points_storage.increment_bad_ass_points_by(21)

    def subtract_reward_cost(self, number):
        self.bad_ass_points_storage.decrement_bad_ass_points_by(number)
