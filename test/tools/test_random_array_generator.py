from src.tools.random_array_generator import Generator
import unittest


class TestRandomArrayGenerator(unittest.TestCase):

    def test_less_than(self):
        less_than = 100
        for i in Generator(10000, less_than).get():
            assert i < less_than

    def test_more_than(self):
        more_than = 50
        for i in Generator(10000, more_than).get():
            assert i > more_than


    def test_amount(self):
        amount = 10
        self.assertEqual(amount, len(Generator(amount, 10).get()))


if __name__ == '__main__':
    unittest.main()
