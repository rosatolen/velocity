class BadAssPointsPurse:
    def __init__(self, bad_ass_points_storage):
        self.bad_ass_points_storage = bad_ass_points_storage
        self.total = self.bad_ass_points_storage.get_bad_ass_points_total()
        if self.total is None:
            self.bad_ass_points_storage.initialize_bad_ass_points()
            self.total = 0

    def add_bad_ass_points_for(self, task):
        if task.is_snail():
            self.bad_ass_points_storage.increment_bad_ass_points_by(1)
        else:
            self.bad_ass_points_storage.increment_bad_ass_points_by(10)
