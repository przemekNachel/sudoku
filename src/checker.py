import src.formatter


def horizontal_lines_correct(sudoku):
    for line in src.formatter.convert_to_lines(sudoku):
        digits = line.replace(".", "")
        if len(digits) != len(set(digits)):
            return False
    return True
