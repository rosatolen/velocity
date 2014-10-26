class SnailTask:
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.__dict__ == other.__dict__
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def is_snail(self):
        return True


class QuailTask:
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.__dict__ == other.__dict__
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def is_snail(self):
        return False
