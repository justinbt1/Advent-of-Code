import numpy as np


def validate_tile(lava_map, m, n, y, x):
    if y < 0 or x < 0:
        return
    if y >= len(lava_map) or x >= len(lava_map[0]):
        return
    if lava_map[y][x] == '.':
        return
    if int(lava_map[y][x]) == int(lava_map[m][n]) + 1:
        return True
    

def walk_trails_heads(lava_map, m, n, trail_count):
    if not isinstance(trail_count, set):
        trail_count = set()

    if lava_map[m][n] == '9':
        trail_count.add((m, n))
        return trail_count

    if validate_tile(lava_map, m, n, m - 1, n):
        trail_count = walk_trails_heads(lava_map, m - 1, n, trail_count)
    if validate_tile(lava_map, m, n, m + 1, n):
        trail_count = walk_trails_heads(lava_map, m + 1, n, trail_count)
    if validate_tile(lava_map, m, n, m, n + 1):
        trail_count = walk_trails_heads(lava_map, m, n + 1, trail_count)
    if validate_tile(lava_map, m, n, m, n - 1):
        trail_count = walk_trails_heads(lava_map, m, n - 1, trail_count)

    return trail_count


def walk_trails_all(lava_map, m, n, trail_count):
    if lava_map[m][n] == '9':
        return trail_count + 1

    if validate_tile(lava_map, m, n, m - 1, n):
        trail_count = walk_trails_all(lava_map, m - 1, n, trail_count)
    if validate_tile(lava_map, m, n, m + 1, n):
        trail_count = walk_trails_all(lava_map, m + 1, n, trail_count)
    if validate_tile(lava_map, m, n, m, n + 1):
        trail_count = walk_trails_all(lava_map, m, n + 1, trail_count)
    if validate_tile(lava_map, m, n, m, n - 1):
        trail_count = walk_trails_all(lava_map, m, n - 1, trail_count)

    return trail_count


def part_one(lava_map):
    good_trails = 0
    trailheads = np.where(lava_map == '0')
    trail_ms, trail_ns = trailheads
    good_trails = 0
    for m, n in zip(trail_ms, trail_ns):
        test = walk_trails_heads(lava_map, m, n, None)
        good_trails += len(test)

    print(good_trails)


def part_two(lava_map):
    good_trails = 0
    trailheads = np.where(lava_map == '0')
    trail_ms, trail_ns = trailheads
    good_trails = 0
    for m, n in zip(trail_ms, trail_ns):
        test = walk_trails_all(lava_map, m, n, 0)
        good_trails += test

    print(good_trails)


if __name__ == '__main__':
    with open('2024/data/10.txt', 'rt') as file:
        lava_map = np.array([list(row.strip()) for row in file])

    part_one(lava_map)
    part_two(lava_map)
