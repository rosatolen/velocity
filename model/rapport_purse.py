class RapportPurse:
    def __init__(self, rapport_storage):
        self.rapport_storage = rapport_storage
        self.total = self.rapport_storage.get_total()
        if self.total is None:
            self.rapport_storage.initialize_rapport({'total': 0})
            self.total = 0

    def add_rapport_for(self, task):
        if task.is_snail():
            self.rapport_storage.increment_rapport_by(1)
        else:
            self.rapport_storage.increment_rapport_by(10)
