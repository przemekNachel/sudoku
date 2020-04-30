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
        string += place(sudoku[i])
        if x < 2:
            string += " "
        x += 1
    return string + "|\n" + BAR


def place(str):
    if str == ".":
        return " "
    return str


def convert_to_lines(sudoku):
    return [sudoku[i:i+9] for i in range(0, len(sudoku), 9)]


def convert_to_string(list):
    return "".join(list)


def convert_to_colums(sudoku):
    return [sudoku[i:len(sudoku):9] for i in range(0, 9)]


# def convert_to_squares(sudoku):
#     return [sudoku[0:27:9] + sudoku[9:], sudoku[1:81:9], sudoku[2:81:9], sudoku[3:81:9], sudoku[4:81:9], sudoku[5:81:9], sudoku[6:81:9], sudoku[7:81:9], sudoku[8:81:9]]