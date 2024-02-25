import unittest
from lab1.src.algo1_2_2 import *


class TestIsListMonotonic(unittest.TestCase):
    def test_if_list_is_increasing(self):
        result = is_list_monotonic([1, 3, 5, 4, 2, 8, 3, 7])
        self.assertEqual(result, False)

    def test_if_list_is_decreasing(self):
        result = is_list_monotonic([9, 8, 5, 5, 5, 2, 1, 1])
        self.assertEqual(result, True)

    def test_if_list_has_one_element(self):
        result = is_list_monotonic([1])
        self.assertEqual(result, True)

    def test_when_list_has_the_same_elements(self):
        result = is_list_monotonic([1,1,1,1,1])
        self.assertEqual(result, True)

    def test_when_list_is_empty(self):
        result = is_list_monotonic([])
        self.assertEqual(result, True)


if __name__ == "__main":
    unittest.main()
