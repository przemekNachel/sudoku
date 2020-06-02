import src.view.main_menu
from src.model.board import Board
from src.resolver.last_possible import LastPossible


class MainMenu:

    def __init__(self, sudoku=None):
        self.view = src.view.main_menu.MainMenu()
        self.sudoku = sudoku
        if self.sudoku is None:
            self.sudoku = self.view.get_sudoku_from_user()
        self.message = ""
        self.board = Board(self.sudoku)
        self.resolver = LastPossible(self.board)

    def start(self):
        while self.view.choice != "exit":
            self.view.get_choice(self.sudoku, self.message)
            self.message = ""
            self.do(self.view.choice)
            print(self.view.choice)

    def do(self, action):
        if action == "scan":
            self.scan()
        if action == "commit":
            self.commit()

    def scan(self):
        self.resolver.scan_all()
        self.message = "To commit: {}".format(self.resolver.to_commit)

    def commit(self):
        self.resolver.commit()
        self.message = "Committed: {}".format(self.resolver.committed)