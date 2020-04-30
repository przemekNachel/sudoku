import src.formatter
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
        self.assertEqual(expected, src.formatter.format(sudoku))

    def test_convert_to_lines(self):
            sudoku = "...9.......857...3......2819......6.....1.7.8..3....95..1.53.798.....51.6........"
            expected = ["...9.....", "..857...3", "......281", "9......6.", "....1.7.8", "..3....95",
                        "..1.53.79", "8.....51.", "6........"]
            self.assertEqual(expected, src.formatter.convert_to_lines(sudoku))

    def test_convert_to_columns(self):
        sudoku = "...9.......857...3......2819......6.....1.7.8..3....95..1.53.798.....51.6........"
        expected = ['...9...86', '.........', '.8...31..', '95.......', '.7..1.5..', '......3..', '..2.7..5.',
                    '..86.971.', '.31.859..']
        self.assertEqual(expected, src.formatter.convert_to_colums(sudoku))

    def test_convert_to_string(self):
        list = ["...9.....", "..857...3", "......281", "9......6.", "....1.7.8", "..3....95", "..1.53.79",
                "8.....51.", "6........"]
        expected = "...9.......857...3......2819......6.....1.7.8..3....95..1.53.798.....51.6........"
        self.assertEqual(expected, src.formatter.convert_to_string(list))

    # def test_convert_to_squares(self):
    #     list = ["...9.....", "..857...3", "......281", "9......6.", "....1.7.8", "..3....95", "..1.53.79",
    #             "8.....51.", "6........"]
    #     expected = "...9.......857...3......2819......6.....1.7.8..3....95..1.53.798.....51.6........"
    #     self.assertEqual(expected, src.formatter.convert_to_squares(list))


if __name__ == '__main__':
    unittest.main()