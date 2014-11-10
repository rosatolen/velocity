from datetime import date


class Purse():
    def __init__(self, total, todays_total, last_updated_day):
        self.total = int(total)
        self.last_updated_day = last_updated_day
        if date.today() == last_updated_day:
            self.todays_total = int(todays_total)
        else:
            self.todays_total = 0

    def add(self, number):
        self.total += number
        self.todays_total += number

        if date.today() > self.last_updated_day:
            self.last_updated_day = date.today()

    def subtract(self, number):
        self.total -= number

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.__dict__ == other.__dict__
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)
