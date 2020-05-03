import src.model.field
import src.tools.formatter


class Board:

    def __init__(self, sudoku="................................................................................."):
        self.fields = self.init_board(sudoku)

    def init_board(self, sudoku):
        fields = []
        for i in range(0, 81):
            fields.append(src.model.field.Field(i, sudoku[i]))
        return tuple(fields)

    def get(self, square, field):
        return src.tools.formatter.convert_to_squares(self.fields)[square-1][field-1]

    def get_line(self, field):
        line = int(field.id / 9)
        return src.tools.formatter.convert_to_lines(self.fields)[line]

    def get_column(self, field):
        column = int(field.id % 9)
        return src.tools.formatter.convert_to_columns(self.fields)[column]

    def to_ascii(self):
        return src.tools.formatter.format(str(self))

    def __str__(self):
        return "".join([str(f) for f in self.fields])

