import src.model.board
from src.tools.random_array_generator import Generator
import unittest


class TestBoard(unittest.TestCase):

    def test_get_1(self):
        board = src.model.board.Board("839162547274985316516437892142378965785629134693541728328714659451896273967253481")
        expected = "1"
        self.assertEqual(expected, str(board.get(square=9, field=9)))

    def test_get_2(self):
        board = src.model.board.Board("839162547274985316516437892142378965785629134693541728328714659451896273967253481")
        expected = "2"
        self.assertEqual(expected, str(board.get(square=5, field=5)))

    def test_get_3(self):
        board = src.model.board.Board("839162547274985316516437892142378965785629134693541728328714659451896273967253481")
        expected = "7"
        self.assertEqual(expected, str(board.get(square=3, field=3)))

    def test_get_4(self):
        board = src.model.board.Board("839162547274985316516437892142378965785629134693541728328714659451896273967253481")
        expected = "4"
        self.assertEqual(expected, str(board.get(square=4, field=2)))

    def test_get_line_1(self):
        board = src.model.board.Board("839162547274985316516437892142378965785629134693541728328714659451896273967253481")
        field = board.get(1, 1)
        expected = "839162547"
        self.assertEqual(expected, "".join([b.value for b in board.get_line(field)]))

    def test_get_line_2(self):
        board = src.model.board.Board("839162547274985316516437892142378965785629134693541728328714659451896273967253481")
        field = board.get(4, 4)
        expected = "785629134"
        self.assertEqual(expected, "".join([b.value for b in board.get_line(field)]))

    def test_get_column_1(self):
        board = src.model.board.Board("839162547274985316516437892142378965785629134693541728328714659451896273967253481")
        field = board.get(2, 6)
        expected = "257891463"
        self.assertEqual(expected, "".join([b.value for b in board.get_column(field)]))

    def test_get_column_2(self):
        board = src.model.board.Board("839162547274985316516437892142378965785629134693541728328714659451896273967253481")
        field = board.get(7, 2)
        expected = "371489256"
        self.assertEqual(expected, "".join([b.value for b in board.get_column(field)]))

    def test_update_possible_values_1(self):
        board = src.model.board.Board("...9.......857...3......2819......6.....1.7.8..3....95..1.53.798.....51.6........")
        expected = set(["1", "2", "3", "4", "5", "7"])
        self.assertEqual(expected, board.get(1, 1).possible_values)

    def test_update_possible_values_2(self):
        board = src.model.board.Board("...9.......857...3......2819......6.....1.7.8..3....95..1.53.798.....51.6........")
        expected = set(["2", "4", "6", "8"])
        self.assertEqual(expected, board.get(5, 8).possible_values)

    def test_update_possible_values_3(self):
        board = src.model.board.Board("...9.......857...3......2819......6.....1.7.8..3....95..1.53.798.....51.6........")
        expected = set(["2", "3", "4"])
        self.assertEqual(expected, board.get(6, 5).possible_values)

    def test_get_square_1(self):
        board = src.model.board.Board("839162547274985316516437892142378965785629134693541728328714659451896273967253481")
        field = board.get(4, 1)
        expected = "142785693"
        self.assertEqual(expected, "".join([b.value for b in board.get_square(field)]))

    def test_get_square_2(self):
        board = src.model.board.Board("839162547274985316516437892142378965785629134693541728328714659451896273967253481")
        field = board.get(6, 3)
        expected = "965134728"
        self.assertEqual(expected, "".join([b.value for b in board.get_square(field)]))

    def test_get_square_3(self):
        board = src.model.board.Board("839162547274985316516437892142378965785629134693541728328714659451896273967253481")
        field = board.get(7, 7)
        expected = "328451967"
        self.assertEqual(expected, "".join([b.value for b in board.get_square(field)]))

    def test_get_square_4(self):
        board = src.model.board.Board("839162547274985316516437892142378965785629134693541728328714659451896273967253481")
        field = board.get(1, 8)
        expected = "839274516"
        self.assertEqual(expected, "".join([b.value for b in board.get_square(field)]))

    def test_get_square_by_field_id(self):
        for i in range(100):
            board = src.model.board.Board(str(Generator(81, 1, 10)))
            square = Generator(1, 1, 10).get()[0]
            field = board.get(square, Generator(1, 1, 10).get()[0])
            self.assertEqual(square, board.get_square_by_field_id(field.id))


if __name__ == '__main__':
    unittest.main()
