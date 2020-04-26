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

if __name__ == '__main__':
    unittest.main()