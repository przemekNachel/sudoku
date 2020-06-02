import src.tools.formatter


class MainMenu:

    menu = "Sudoku Resolver\n{message}\n{sudoku}\n1. Scan\n2. Commit\n\n0. Exit"

    def __init__(self):
        self.choice = None

    def get_sudoku_from_user(self):
        return input("Enter sudoku in one line format:\n")

    def get_choice(self, sudoku, message=""):
        choice_string = input(MainMenu.menu.format(message=message, sudoku=src.tools.formatter.format(sudoku)))
        if choice_string == "1":
            self.choice = "scan"
        elif choice_string == "2":
            self.choice = "commit"
        elif choice_string == "0":
            self.choice = "exit"
        else:
            self.choice = None

