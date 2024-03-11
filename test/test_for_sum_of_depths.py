import unittest
from src.the_sum_of_depths import *

class TestIsListMonotonic(unittest.TestCase):
    def test1(self):
        root = Node(3)
        root.left = Node(9)
        root.right = Node(20)
        self.assertEqual(sum_of_depths(root), 2)

    def test2(self):
        root = Node(3)
        root.left = Node(9)
        root.right = Node(20)
        root.right.right = Node(22)
        root.right.left = Node(10)
        root.left.left = Node(8)
        root.left.right = Node(11)
        self.assertEqual(sum_of_depths(root), 10)

    def test3(self):
        root = Node()
        self.assertEqual(sum_of_depths(root), 0)


