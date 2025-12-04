import numpy as np
from numpy.lib.stride_tricks import sliding_window_view


def read_data():
    with open('2025/data/4.txt', 'rt') as pattern_buffer:
        matrix = []
        for row in pattern_buffer:
            matrix.append([int(i) for i in list(row.strip().replace('.', '0').replace('@', '1'))])
        return np.array(matrix)


def convolve(matrix, removal=False):
    windows = sliding_window_view(matrix, window_shape=(3, 3), writeable=removal)
    reachable = 0
    for row in windows:
        for kernel in row:
            if kernel[1][1]:
                if np.sum(kernel) < 5:
                    reachable += 1
                    if removal:
                        kernel[1][1] = 0

    return reachable


def part_1(data):
    reachable = convolve(data)
    print(reachable)


def part_2(data):
    reachable = 0
    while True:
        reached = convolve(data, removal=True)
        reachable += reached
        if reached == 0:
            break
    print(reachable)


if __name__ == '__main__':
    data = np.pad(read_data(), (1, 1))
    part_1(data)
    part_2(data)
