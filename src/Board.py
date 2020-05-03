import src.Field


class Board:

    def __init__(self, sudoku="................................................................................."):
        self.fields = self.init_board(sudoku)

    def init_board(self, sudoku):
        fields = []
        for i in range(0, 81):
            fields.append(src.Field.Field(i, sudoku[i]))
        return tuple(fields)

    def __str__(self):
        return "".join([str(f) for f in self.fields])
