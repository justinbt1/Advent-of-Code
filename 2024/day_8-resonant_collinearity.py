
from collections import defaultdict

def find_antennas(matrix):
    antennas = defaultdict(list)
    for m in range(len(matrix)):
        for n in range(len(matrix[0])):
            if matrix[m][n] != '.':
                antennas[matrix[m][n]].append(([m, n]))

    return antennas


def find_antinodes(antena_positions):
    antinodes = set()
    for frequency in antena_positions:
        positions = antena_positions[frequency]
        for _ in range(len(positions) - 1):
            m, n = positions.pop()
            for y, x in positions:
                mn_antinode = (m + (m - y), (n + (n - x)))
                xy_antinode = (y + (y - m), (x + (x - n)))
                
                for antinode in [mn_antinode, xy_antinode]:
                    if any(n < 0 for n in antinode):
                        continue
                    if antinode[0] < len(matrix) and antinode[1] < len(matrix[0]):
                        antinodes.add(antinode)

    print(len(antinodes))


if __name__ == '__main__':
    matrix = []
    with open('2024/data/8.txt', 'rt') as file:
        for row in file:
            matrix.append(list(row.strip()))

    antenas = find_antennas(matrix)
    find_antinodes(antenas)
