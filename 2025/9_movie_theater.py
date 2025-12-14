import numpy as np


def load_data():
    coordinates = []
    with open('2025/data/9.txt', 'rt') as buffer:
        for line in buffer.read().splitlines():
            coordinates.append(np.array([int(i) for i in line.split(',')]))

    return coordinates


def part_one(red_tiles):
    max_area = 0
    for _ in range(len(red_tiles) - 1):
        coord_a = red_tiles.pop()
        for coord_b in red_tiles:
            area = np.prod(np.abs(coord_a - coord_b) + 1)
            if area > max_area:
                max_area = area

    print(max_area)


if __name__ == '__main__':
    red_tiles = load_data()
    part_one(red_tiles)
