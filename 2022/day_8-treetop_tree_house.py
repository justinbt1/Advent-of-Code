def create_grid():
    grid = []
    with open('data/8.txt', 'rt') as input_file:
        for line in input_file:
            grid.append(list(line.strip()))

    return grid


def walk_rows(row, i, results):
    previous_tree = row[0]
    for j in range(1, len(row), 1):
        if row[j] > previous_tree:
            results[i][j] = 1
            previous_tree = row[j]

    previous_tree = row[-1]
    for j in range(len(row) - 1, 0, -1):
        if row[j] > previous_tree:
            results[i][j] = 1
            previous_tree = row[j]


def brute_force_visibility_scan(grid, results):
    for i in range(1, len(grid) - 1):
        results[i][0] = 1
        results[i][-1] = 1
        walk_rows(grid[i], i, results)

    for j in range(1, len(grid[0]) - 1):
        previous_tree = grid[0][j]
        for i in range(1, len(grid) - 1):
            if grid[i][j] > previous_tree:
                results[i][j] = 1
                previous_tree = grid[i][j]

    for j in range(1, len(grid[0]) - 1):
        previous_tree = grid[-1][j]
        for i in range(len(grid) - 1, 1, -1):
            if grid[i][j] > previous_tree:
                results[i][j] = 1
                previous_tree = grid[i][j]

    total = 0
    for r in results:
        total += sum(r)

    print(total)


if __name__ == '__main__':
    tree_grid = create_grid()
    results_grid = [[1 for i in range(len(tree_grid[1]))]]
    results_grid += [
        [0 for i in range(len(tree_grid[0]))] for i in range(len(tree_grid) - 2)
    ]
    results_grid += [[1 for i in range(len(tree_grid[1]))]]
    brute_force_visibility_scan(tree_grid, results_grid)
