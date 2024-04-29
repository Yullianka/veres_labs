class DisjointSet:
    def __init__(self, vertices):
        self.parent = {}
        self.rank = {}
        self.edges = []
        for vertex in vertices:
            self.parent[vertex] = vertex
            self.rank[vertex] = 0

    def find(self, vertex):
        if self.parent[vertex] != vertex:
            self.parent[vertex] = self.find(self.parent[vertex])
        return self.parent[vertex]

    def union(self, vertex1, vertex2):
        root1 = self.find(vertex1)
        root2 = self.find(vertex2)

        if root1 != root2:
            if self.rank[root1] < self.rank[root2]:
                self.parent[root1] = root2
            elif self.rank[root1] > self.rank[root2]:
                self.parent[root2] = root1
            else:
                self.parent[root1] = root2
                self.rank[root2] += 1

    def add_edge(self, source, destination, weight):
        self.edges.append((source, destination, weight))

    def get_edges(self):
        return self.edges



def kruskal(graph):
    edges = graph.get_edges()
    edges.sort(key=lambda edge: edge[2])

    min_spanning_tree = []
    for edge in edges:
        source, destination, weight = edge

        root1 = graph.find(source)
        root2 = graph.find(destination)
        if root1 != root2:
            min_spanning_tree.append((source, destination, weight))
            graph.union(source, destination)

    return min_spanning_tree


def min_optical_cable_length(graph):
    mst = kruskal(graph)
    total_length = 0

    for edge in mst:
        source, destination, weight = edge
        total_length += weight

    return total_length
