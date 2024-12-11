import numpy as np


def validate_tile(lava_map, m, n, y, x):
    if y < 0 >= len(lava_map) or x < 0:
        return
    if y >= len(lava_map) or x >= len(lava_map[0]):
        return
    if lava_map[y][x] == '.':
        return
    if int(lava_map[y][x]) == int(lava_map[m][n]) + 1:
        return True


def walk_trails_heads(lava_map, m, n, part_two, trail_count):
    if not part_two and not isinstance(trail_count, set):
        trail_count = set()

    if lava_map[m][n] == '9':
        if not part_two:
            trail_count.add((m, n))
            return trail_count
        else:
            return trail_count + 1

    for i in [(m - 1, n), (m + 1, n), (m, n + 1), (m, n - 1)]:
        if validate_tile(lava_map, m, n, i[0], i[1]):
            trail_count = walk_trails_heads(
                lava_map, i[0], i[1], part_two, trail_count)

    return trail_count


def count_good_trails(lava_map, part_two=False):
    good_trails = 0
    trail_ms, trail_ns = np.where(lava_map == '0')
    for m, n in zip(trail_ms, trail_ns):
        test = walk_trails_heads(lava_map, m, n, part_two, 0)
        if not part_two:
            test = len(test)
        good_trails += test

    print(good_trails)


if __name__ == '__main__':
    with open('2024/data/10.txt', 'rt') as file:
        lava_map = np.array([list(row.strip()) for row in file])

    count_good_trails(lava_map)
    count_good_trails(lava_map, part_two=True)
