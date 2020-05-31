from src.tools.random_array_generator import Generator
import unittest


class TestRandomArrayGenerator(unittest.TestCase):

    def test_less_than(self):
        less_than = 10
        for i in Generator(10000, 0, less_than).get():
            assert i < less_than

    def test_more_than(self):
        starts_from = 0
        for i in Generator(10000, starts_from, 10).get():
            assert i >= starts_from

    def test_amount(self):
        amount = 10
        self.assertEqual(amount, len(Generator(amount, 0, 10).get()))


if __name__ == '__main__':
    unittest.main()
