from src.model.field import Field
import src.tools.formatter as formatter
import math


class Board:

    def __init__(self, sudoku="................................................................................."):
        self.fields = self.init_board(sudoku)

    def init_board(self, sudoku):
        fields = []
        for i in range(0, 81):
            fields.append(Field(i, sudoku[i]))
        return tuple(fields)

    def get(self, square, field):
        field = formatter.convert_to_squares(self.fields)[square-1][field-1]
        self.update_possible_values(field)
        return field

    def get_line(self, field):
        line = int(field.id / 9)
        return formatter.convert_to_lines(self.fields)[line]

    def update_possible_values(self, field):
        line = [i.value for i in self.get_line(field)]
        column = [i.value for i in self.get_column(field)]
        square = [i.value for i in self.get_square(field)]
        not_possible = set(list(line+column+square))
        if "." in not_possible:
            not_possible.remove(".")
        field.possible_values = set(field.possible_values) - not_possible

    def get_column(self, field):
        column = field.id % 9
        return formatter.convert_to_columns(self.fields)[column]

    def get_square_by_field_id(self, id):
        x = (id % 9) + 1
        y = int(id / 9) + 1
        x = math.floor(x / 3 - 0.01) + 1
        y = math.floor(y / 3 - 0.01) + 1
        square = (3 * y) - 3 + x
        return square

    def get_square(self, field):
        return formatter.convert_to_squares(self.fields)[self.get_square_by_field_id(field.id) - 1]

    def to_ascii(self):
        return formatter.format(str(self))

    def __str__(self):
        return "".join([str(f) for f in self.fields])


