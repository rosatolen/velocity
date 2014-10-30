from pymongo import MongoClient


class TestStorageAccess:
    def __init__(self):
        self.bad_ass_points = MongoClient('mongodb://localhost:27017').velocity.bad_ass_points

    def set_bad_ass_points(self, number):
        i = self.bad_ass_points.distinct('total').pop()
        self.bad_ass_points.update({'total': i}, {'$set': {'total': number}})
