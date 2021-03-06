import src.tools.formatter
import src.model.board
import unittest


class TestFormatter(unittest.TestCase):

    def test_format(self):
        sudoku = "...9.......857...3......2819......6.....1.7.8..3....95..1.53.798.....51.6........"
        expected = """
 ----------------- 
|     |9    |     |
|    8|5 7  |    3|
|     |     |2 8 1|
|-----+-----+-----|
|9    |     |  6  |
|     |  1  |7   8|
|    3|     |  9 5|
|-----+-----+-----|
|    1|  5 3|  7 9|
|8    |     |5 1  |
|6    |     |     |
 ----------------- 
"""
        self.assertEqual(expected, src.tools.formatter.format(sudoku))

    def test_convert_to_lines(self):
        sudoku = "...9.......857...3......2819......6.....1.7.8..3....95..1.53.798.....51.6........"
        expected = ["...9.....", "..857...3", "......281", "9......6.", "....1.7.8", "..3....95",
                    "..1.53.79", "8.....51.", "6........"]
        self.assertEqual(expected, src.tools.formatter.convert_to_lines(str(src.model.board.Board(sudoku))))

    def test_convert_to_columns(self):
        sudoku = "...9.......857...3......2819......6.....1.7.8..3....95..1.53.798.....51.6........"
        expected = ['...9...86', '.........', '.8...31..', '95.......', '.7..1.5..', '......3..', '..2.7..5.',
                    '..86.971.', '.31.859..']
        self.assertEqual(expected, src.tools.formatter.convert_to_columns(str(src.model.board.Board(sudoku))))

    def test_convert_to_squares(self):
        sudoku = "...9.......857...3......2819......6.....1.7.8..3....95..1.53.798.....51.6........"
        expected = ['.....8...', '9..57....', '.....3281', '9.......3', '....1....', '.6.7.8.95', '..18..6..',
                    '.53......', '.7951....']
        self.assertEqual(expected, src.tools.formatter.convert_to_squares(str(src.model.board.Board(sudoku))))

    def test_convert_to_string(self):
        list = ["...9.....", "..857...3", "......281", "9......6.", "....1.7.8", "..3....95", "..1.53.79",
                "8.....51.", "6........"]
        expected = "...9.......857...3......2819......6.....1.7.8..3....95..1.53.798.....51.6........"
        self.assertEqual(expected, src.tools.formatter.convert_to_string(list))


if __name__ == '__main__':
    unittest.main()
