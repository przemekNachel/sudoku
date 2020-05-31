from random import randrange

class Generator:

    def __init__(self, amount, less_than):
        self.amount = amount
        self.less_than = less_than

    def get(self):
        return [randrange(self.less_than) for i in range(self.amount)]


