import unittest

from src.knuth_morris_pratt import *


class TestCareerGraph(unittest.TestCase):
    def test1(self):
        needle = "baboab"
        haystack = " bababa baboab "
        result = kmp(haystack, needle)
        self.assertEqual(result, [8])

    def test2(self):
        needle = " "
        haystack = " "
        result = kmp(haystack, needle)
        self.assertEqual(result, [0])

    def test3(self):
        needle = " abc "
        haystack = " sadab abc "
        result = kmp(haystack, needle)
        self.assertEqual(result, [6])


