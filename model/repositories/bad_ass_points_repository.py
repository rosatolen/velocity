class BadAssPointsRepository:
    def __init__(self, mongo_repository):
        self.mongo_repository = mongo_repository

    def increment_bad_ass_points_by(self, number):
        self.mongo_repository.increment_bad_ass_points_by(number)

    def get_bad_ass_points_total(self):
        total = self.mongo_repository.get_bad_ass_points_total('total')
        if not total:
            return None
        else:
            return total.pop()

    def initialize_bad_ass_points(self):
        self.mongo_repository.initialize_bad_ass_points({'total': 0})
