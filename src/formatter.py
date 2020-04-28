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
    else:
        return str
    return string


def convert_to_2dtable(sudoku):
    return [list(sudoku[0:9]), list(sudoku[9:18]), list(sudoku[18:27]), list(sudoku[27:36]), list(sudoku[36:45]), list(sudoku[45:54]), list(sudoku[54:63]), list(sudoku[63:72]), list(sudoku[72:81])]
