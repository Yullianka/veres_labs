import unittest
from src.iot_telecoms import *


class TestPrimAlgorithm(unittest.TestCase):
    @staticmethod
    def load_graph_from_csv(filepath):
        vertices = set()
        edges = []
        with open(filepath, 'r') as file:
            for line in file:
                parts = line.strip().split(',')
                source, destination, weight = parts[0], parts[1], int(parts[2])
                vertices.update([source, destination])
                edges.append((source, destination, weight))
        graph = DisjointSet(list(vertices))
        for source, destination, weight in edges:
            graph.add_edge(source, destination, weight)
        return graph

    def test1(self):
        file_path = "test/resources/communication_wells.csv"
        graph = self.load_graph_from_csv(file_path)
        find_cable_length = min_optical_cable_length(graph)
        self.assertEqual(29, find_cable_length)

    def test2(self):
        file_path = "test/resources/communication_wells2.csv"
        graph = self.load_graph_from_csv(file_path)
        find_cable_length = min_optical_cable_length(graph)
        self.assertEqual(2, find_cable_length)





if __name__ == '__main__':
    unittest.main()
