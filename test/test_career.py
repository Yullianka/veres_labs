import unittest

from src.career import max_experience, build_graph

class TestCareerGraph(unittest.TestCase):
    def test_career_graph_1(self):
        levels = [
            [4],
            [3, 1],
            [2, 1, 5],
            [1, 3, 2, 1]
        ]
        organization_graph = build_graph(levels)
        result = max_experience(organization_graph)
        self.assertEqual(result, 12)

    def test_max_experience_with_negative_values(self):
        levels = [
            [10],
            [12, 15],
            [18, 48, 2],
            [1, 3, 5, 120]
        ]
        organization_graph = build_graph(levels)
        result = max_experience(organization_graph)
        self.assertEqual(result, 147)

    def test_max_experience_with_empty_graph(self):
        levels = []
        organization_graph = build_graph(levels)
        result = max_experience(organization_graph)
        self.assertEqual(result, 0)


if __name__ == "__main__":
    unittest.main()
