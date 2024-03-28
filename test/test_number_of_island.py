import unittest
import os
from src.number_of_islands import *

cur_path = os.path.dirname(__file__)


class TestFindTheNuberOfIslands(unittest.TestCase):
    def test1(self):
        number_of_islands(cur_path + "\\resources\\input.txt", cur_path + "\\resources\\output.txt")
        with open(cur_path + "\\resources\\output.txt", "r", encoding="utf-8") as file:
            first_line = file.readline()
        self.assertEqual(int(first_line), 3)

    def test2(self):
        number_of_islands(cur_path + "\\resources\\input2.txt", cur_path + "\\resources\\output2.txt")
        with open(cur_path + "\\resources\\output2.txt", "r", encoding="utf-8") as file:
            first_line = file.readline()
        self.assertEqual(int(first_line), -1)

    def test3(self):
        number_of_islands(cur_path + "\\resources\\input3.txt", cur_path + "\\resources\\output3.txt")
        with open(cur_path + "\\resources\\output3.txt",  "r", encoding="utf-8", ) as file:
            first_line = file.readline()
        self.assertEqual(int(first_line), 3)


if __name__ == "__main__":
    unittest.main()
