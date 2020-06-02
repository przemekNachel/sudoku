import src.view.main_menu

class MainMenu:

    def __init__(self, sudoku=None):
        self.view = src.view.main_menu.MainMenu()
        self.sudoku = sudoku
        if self.sudoku is None:
            self.sudoku = self.view.get_sudoku_from_user()

    def start(self):
        while self.view.choice != "exit":
            self.view.get_choice(self.sudoku)
            self.do(self.view.choice)

    def do(self, action):
        if action == "scan":
            self.scan()

    def scan(self):
        pass
