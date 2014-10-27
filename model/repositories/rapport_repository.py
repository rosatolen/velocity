class RapportRepository:
    def __init__(self, mongo_repository):
        self.mongo_repository = mongo_repository

    def increment_rapport_by(self, number):
        self.mongo_repository.increment_rapport_total_by(number)

    def get_rapport_total(self):
        total = self.mongo_repository.get('total')
        if not total:
            return None
        else:
            return total.pop()

    def initialize_rapport(self):
        self.mongo_repository.initialize_rapport({'total': 0})
