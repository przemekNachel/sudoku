BAR = " ----------------- \n"
LINE = "|-----+-----+-----|\n"


def format(sudoku):
    x = 0
    string = "\n" + str(BAR)
    for i in range(0, 81):
        if x == 3:
            x = 0
        if i != 0:
            if i % 3 == 0:
                string += "|"
            if i % 9 == 0:
                string += "\n"
            if i % 27 == 0:
                string += LINE
        if i % 9 == 0:
            string += "|"
        string += sudoku[i]
        if x < 2:
            string += " "
        x += 1
    return string.replace(".", " ") + "|\n" + BAR


def get_point_in_sudoku(id):
    sudoku = "." * 81
    return sudoku[:id] + "x" + sudoku[id + 1:]


def convert_to_lines(sudoku):
    return [sudoku[i:i+9] for i in range(0, len(sudoku), 9)]


def convert_to_string(list):
    return "".join(list)


def convert_to_columns(sudoku):
    return [sudoku[i:len(sudoku):9] for i in range(0, 9)]


def convert_to_squares(sudoku):
    squares = []
    for i in range(0, len(sudoku), 27):
        for j in range(i, i+9, 3):
            lines = []
            for k in range(j, j+19, 9):
                lines.append(sudoku[k:k+3])
            squares.append(lines[0] + lines[1] + lines[2])
    return squares
