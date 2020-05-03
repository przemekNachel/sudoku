class Field:

    def __init__(self, i, value):
        self.id = i
        self.value = value
        self.possible_values = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

    def __str__(self):
        return self.value
