import unittest
from src.min_size_of_board import *

class TestMinSize(unittest.TestCase):
    def test1(self):
        result = min_size(10,2,3)
        self.assertEqual(result, 9)

    def test2(self):
        result = min_size(10,7,3)
        self.assertEqual(result,15)

    def test3(self):
        result = min_size(4, 1, 1)
        self.assertEqual(result, 2)

    def test4(self):
        result = min_size(2, 1000000000, 999999999)
        self.assertEqual(result, None)

