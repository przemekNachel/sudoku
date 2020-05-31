import random

class Generator:

    def __init__(self, amount, starts_from, less_than):
        self.amount = amount
        self.starts_from = starts_from
        self.less_than = less_than

    def get(self):
        return [random.randrange(self.starts_from, self.less_than) for i in range(self.amount)]


