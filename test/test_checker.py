import src.checker
import unittest


class TestChecker(unittest.TestCase):

    def test_bad_horizontal_line(self):
        bad_sudoku = "...9.......857...3......2819......6.....1.7.8..3....95..1.53.798.....51.66......."
        self.assertFalse(src.checker.horizontal_lines_correct(bad_sudoku))


if __name__ == '__main__':
    unittest.main()
