import src.model.field
import src.tools.formatter
import math


class Board:

    def __init__(self, sudoku="................................................................................."):
        print(sudoku)
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
        column = field.id % 9
        return src.tools.formatter.convert_to_columns(self.fields)[column]

    def get_square_by_field_id(self, id):
        x = (id % 9) + 1
        y = int(id / 9) + 1
        x = math.floor(x / 3 - 0.01) + 1
        y = math.floor(y / 3 - 0.01) + 1
        square = (3 * y) - 3 + x
        print(src.tools.formatter.format(src.tools.formatter.get_point_in_sudoku(id)))
        print("id = {}\nx = {}\ny = {}\nsquare = {}\n".format(id, x, y, square))
        return square

    def get_square(self, field):
        return src.tools.formatter.convert_to_squares(self.fields)[self.get_square_by_field_id(field.id) - 1]

    def to_ascii(self):
        return src.tools.formatter.format(str(self))

    def __str__(self):
        return "".join([str(f) for f in self.fields])


