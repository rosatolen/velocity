class Reward:
    def __init__(self, name, cost):
        self.name = name
        self.cost = cost

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.__dict__ == other.__dict__
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)
