def create_grid():
    grid = []
    with open('data/8.txt', 'rt') as input_file:
        for line in input_file:
            grid.append(list(line.strip()))

    return grid


def calculate_view(current_tree, tree_line):
    viewing_distance = 0
    for tree in tree_line:
        viewing_distance += 1
        if tree >= current_tree:
            break

    return viewing_distance


def check_visibility(current_tree, tree_line):
    if not tree_line:
        return True

    if max(tree_line) < current_tree:
        return True


def scan_trees():
    tree_grid = create_grid()
    max_scenic_score = 0
    visible_tree_count = 0
    for i in range(len(tree_grid)):
        for j in range(len(tree_grid[0])):
            current_tree = tree_grid[i][j]
            east = [tree for tree in tree_grid[i][j + 1:]]
            west = [tree_grid[i][t - 1] for t in range(j, 0, -1)]
            north = [tree_grid[t - 1][j] for t in range(i, 0, -1) if t > 0]
            south = [tree_grid[t][j] for t in range(i + 1, len(tree_grid))]

            for direction in [east, west, north, south]:
                if check_visibility(current_tree, direction):
                    visible_tree_count += 1
                    break

            scenic_score = 1
            for direction in [east, west, north, south]:
                scenic_score *= calculate_view(current_tree, direction)

            if scenic_score > max_scenic_score:
                max_scenic_score = scenic_score

    print(f'Part 1: {visible_tree_count}')
    print(f'Part 2: {max_scenic_score}')


if __name__ == '__main__':
    scan_trees()
