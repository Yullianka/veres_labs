import unittest
from src.electricity import *


class TestIsListMonotonic(unittest.TestCase):
    def test1(self):
        distance = 2
        height_of_the_pillars = 2, 3, 3
        result = calculate_rope(distance, height_of_the_pillars)
        self.assertEqual(result, 5.66)

    def test2(self):
        distance = 100
        height_of_the_pillars = 1, 1, 1, 1
        result = calculate_rope(distance, height_of_the_pillars)
        self.assertEqual(result, 300)

    def test3(self):
        distance = 5
        height_of_the_pillars = 5, 10, 15, 20
        result = calculate_rope(distance, height_of_the_pillars)
        self.assertEqual(result, 40.24)