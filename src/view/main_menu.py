import src.tools.formatter


class MainMenu:

    menu = "Sudoku Resolver\n\n{sudoku}\n1. Scan\n\n0. Exit"

    def __init__(self):
        self.choice = None

    def get_sudoku_from_user(self):
        return input("Enter sudoku in one line format:\n")

    def get_choice(self, sudoku):
        choice_string = input(MainMenu.menu.format(sudoku=src.tools.formatter.format(sudoku)))
        if choice_string == "1":
            self.choice = "scan"
        elif choice_string == "0":
            self.choice = "exit"
        else:
            self.choice = None

