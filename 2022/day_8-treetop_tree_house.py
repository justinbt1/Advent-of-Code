
def create_grid():
    grid = []
    with open('data/8.txt', 'rt') as input_file:
        for line in input_file:
            grid.append(list(line.strip()))

    return grid


def create_results_grid(width, height):
    results_grid = [[1 for _ in range(width)]]
    for _ in range(height - 2):
        results_grid.append([0 for _ in range(width)])

    results_grid += [[1 for _ in range(width)]]

    return results_grid


def row_walker(row, i, results, first_row, start, end, step_direction):
    previous_tree = row[first_row]
    for j in range(start, end, step_direction):
        if row[j] > previous_tree:
            results[i][j] = 1
            previous_tree = row[j]


def walk_rows(grid, results):
    for i in range(1, len(grid) - 1):
        results[i][0] = 1
        results[i][-1] = 1
        row_walker(grid[i], i, results, 0, 1, len(grid[i]) - 1, 1)
        row_walker(grid[i], i, results, -1, len(grid[i]) - 1, 1, -1)


def walk_columns(grid, results, first_row, start, end, step_direction):
    for j in range(1, len(grid[0]) - 1):
        previous_tree = grid[first_row][j]
        for i in range(start, end, step_direction):
            if grid[i][j] > previous_tree:
                results[i][j] = 1
                previous_tree = grid[i][j]


def brute_force_visibility_scan(grid, results):
    walk_rows(grid, results)
    walk_columns(grid, results, 0, 1, len(grid) - 1, 1)
    walk_columns(grid, results, -1, len(grid) - 1, 1, -1)

    total = 0
    for r in results:
        total += sum(r)

    print(total)


if __name__ == '__main__':
    tree_grid = create_grid()
    results_grid = create_results_grid(len(tree_grid[0]), len(tree_grid))
    brute_force_visibility_scan(tree_grid, results_grid)
