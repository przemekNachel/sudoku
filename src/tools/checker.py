import src.tools.formatter


def check_sets_are_unique(sets):
    for string in sets:
        digits = string.replace(".", "")
        if len(digits) != len(set(digits)):
            return False
    return True


def horizontal_lines_correct(sudoku):
    return check_sets_are_unique(src.tools.formatter.convert_to_lines(sudoku))


def vertical_lines_correct(sudoku):
    return check_sets_are_unique(src.tools.formatter.convert_to_columns(sudoku))


def squares_correct(sudoku):
    return check_sets_are_unique(src.tools.formatter.convert_to_squares(sudoku))


def is_correct(sudoku):
    return horizontal_lines_correct(sudoku) and vertical_lines_correct(sudoku) and squares_correct(sudoku)
