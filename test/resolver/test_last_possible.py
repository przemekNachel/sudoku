from src.resolver.last_possible import LastPossible
from src.model.board import Board

import unittest


class TestLastPossible(unittest.TestCase):

    def test_scan_1(self):
        resolver = LastPossible(Board("231847965874569231659312487196235874783694512542781396417923658365478129928156743"))
        resolver.scan_all()
        self.assertEqual([], resolver.fields_with_last_possible_value)

    def test_scan_2(self):
        board = Board("23.847965874569231659312487196235874783694512542781396417923658365478129928156743")
        resolver = LastPossible(board)
        resolver.scan_all()
        self.assertEqual(1, len(resolver.fields_with_last_possible_value))
        self.assertEqual(1, resolver.scan_counter)

    def test_scan_2(self):
        board = Board("23.847965874569231659312487196235874783694512542781396417923658365478129928156743")
        resolver = LastPossible(board)
        resolver.scan_all()
        resolver.scan_all()
        self.assertEqual(1, len(resolver.fields_with_last_possible_value))
        self.assertEqual(2, resolver.scan_counter)


if __name__ == '__main__':
    unittest.main()
