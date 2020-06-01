class LastPossible:

    def __init__(self, board):
        self.scan_counter = 0
        self.committed = 0
        self.board = board
        self.fields_with_last_possible_value = []

    def scan_all(self):
        for i in range(1, 10):
            for j in range(1, 10):
                field = self.board.get(i, j)
                if field.value == "." and len(field.possible_values) == 1:
                    self.fields_with_last_possible_value.append(field)
        self.fields_with_last_possible_value = list(set(self.fields_with_last_possible_value))
        self.scan_counter += 1

    def commit(self):
        for field in self.fields_with_last_possible_value:
            field.value = field.possible_values.pop()
            self.committed += 1
