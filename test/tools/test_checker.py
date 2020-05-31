import src.tools.checker
import unittest


class TestChecker(unittest.TestCase):

    def test_bad_horizontal_line(self):
        bad_sudoku = "...9.......857...3......2819......6.....1.7.8..3....95..1.53.798.....51.66......."
        self.assertFalse(src.tools.checker.horizontal_lines_correct(bad_sudoku))

    def test_bad_vertical_line(self):
        bad_sudoku = "...9.......857...3......2819......6.....1.7.8..3....95..1.53.798.....51.6.3......"
        self.assertFalse(src.tools.checker.vertical_lines_correct(bad_sudoku))

    def test_bad_sqare(self):
        bad_sudoku = "...9.......857...3......2819......6.....1.7.8..3....95..1.53.798.....51.6.1......"
        self.assertFalse(src.tools.checker.squares_correct(bad_sudoku))

    def test_good_sudoku(self):
        sudokus = ["653728149824319765791456283216593874437862591985147326362981457578634912149275638",
                   "521367948487925631639841725745218369218639574963754182392586417874193256156472893",
                   "397285416516974283482136597953721864278463951641598732829617345134852679765349128",
                   "193467582724851963586293741265389417947512836318746259839175624652934178471628395",
                   "839162547274985316516437892142378965785629134693541728328714659451896273967253481"]
        for sudoku in sudokus:
            self.assertTrue(src.tools.checker.is_correct(sudoku))


if __name__ == '__main__':
    unittest.main()
