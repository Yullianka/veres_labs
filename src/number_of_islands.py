def bfs(graph, x, y, visited):
    queue = [(y, x)]

    while queue:
        y, x = queue.pop(0)
        visited.add((y, x))
        neighbours = get_neighbours(graph, x, y)
        for neighbour in neighbours:
            if neighbour not in visited:
                queue.append(neighbour)


def get_neighbours(graph, x, y):
    neighbour = []
    direction = [(1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)]

    for cols, rows in direction:
        if len(graph) - 1 >= abs(y + cols) and len(graph) - 1 >= abs(x + rows):
            if graph[abs(y + cols)][abs(x + rows)]:
                neighbour.append((abs(y + cols), abs(x + rows)))
    return neighbour


def number_of_islands(filename_read, filename_write):
    graph = read_input(filename_read)

    if len(graph) == 0 or len(graph[0]) == 0:
        write_output(filename_write, -1)
        return

    row = len(graph)
    col = len(graph[0])
    visited = set()
    count = 0

    for y in range(row):
        for x in range(col):
            if graph[y][x] == 1:
                if (y, x) not in visited:
                    count += 1
                bfs(graph, x, y, visited)
    write_output(filename_write, count)


def read_input(file_name):
    input_matrix = []
    with open(file_name, "r", encoding="utf-8") as file:
        for line in file:
            row = list(map(int, line.split()))
            input_matrix.append(row)
    file.close()
    return input_matrix


def write_output(filename, result):
    with open(filename, "w", encoding="utf-8",) as file:
        file.write(str(result))
