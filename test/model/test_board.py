import src.model.board
import unittest


class TestBoard(unittest.TestCase):

    def test_get(self):
        board = src.model.board.Board("839162547274985316516437892142378965785629134693541728328714659451896273967253481")
        expected = "1"
        self.assertEqual(expected, str(board.get(square=9, field=9)))
        expected = "2"
        self.assertEqual(expected, str(board.get(square=5, field=5)))
        expected = "7"
        self.assertEqual(expected, str(board.get(square=3, field=3)))
        expected = "4"
        self.assertEqual(expected, str(board.get(square=4, field=2)))

    def test_get_line(self):
        board = src.model.board.Board("839162547274985316516437892142378965785629134693541728328714659451896273967253481")
        expected = "839162547"
        self.assertEqual(expected, "".join([b.value for b in board.get_line(1)]))

    # def test_update_possible_values(self):
    #     board = src.model.board.Board("...9.......857...3......2819......6.....1.7.8..3....95..1.53.798.....51.6........")
    #     expected = ["1", "2", "3", "4", "5", "7"]
    #     self.assertEqual(expected, board.get(1, 1).possible_values)

if __name__ == '__main__':
    unittest.main()
