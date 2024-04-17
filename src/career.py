class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def build_graph(levels):
    graph = []
    for row in levels:
        graph_row = []
        for value in row:
            graph_row.append(Node(value))
        graph.append(graph_row)
    for i in range(len(levels) - 1):
        for j in range(len(levels[i])):
            graph[i][j].left = graph[i + 1][j]
            graph[i][j].right = graph[i + 1][j + 1]
    return graph


def max_experience(graph):
    if not graph or not graph[0]:
        return 0
    for i in reversed(range(len(graph) - 1)):
        for j in range(len(graph[i])):
            graph[i][j].value += max(graph[i][j].left.value, graph[i][j].right.value)
    return graph[i][j].value


with open('../test/resources/career.in.txt', 'w') as file:
    file.write("4\n")
    file.write("4\n")
    file.write("3 1\n")
    file.write("2 1 5\n")
    file.write("1 3 2 1\n")

expected_output = "12\n"

with open('../test/resources/career.out.txt', 'w') as file:
    file.write(expected_output)