
from collections import defaultdict

def find_antennas(matrix):
    antennas = defaultdict(list)
    for m in range(len(matrix)):
        for n in range(len(matrix[0])):
            if matrix[m][n] != '.':
                antennas[matrix[m][n]].append(([m, n]))

    return antennas


def iter_nodes(m, n, m_delta, n_delta):
    antinodes = set()
    while True:
        m = m + m_delta
        n = n + n_delta
        mn_antinode = (m, n)
        if any(n < 0 for n in mn_antinode):
            break
        if mn_antinode[0] >= len(matrix) or mn_antinode[1] >= len(matrix[0]):
            break
        antinodes.add(mn_antinode)            

    return antinodes


def find_antinodes(antena_positions):
    antinodes = set()
    for frequency in antena_positions:
        positions = antena_positions[frequency]
        for antena in positions:
            antinodes.add(tuple(antena))
        for _ in range(len(positions) - 1):
            m, n = positions.pop()
            for y, x in positions:
                antinodes.update(iter_nodes(m, n, m - y, n - x))
                antinodes.update(iter_nodes(y, x, y - m, x - n))

    print(len(antinodes))


if __name__ == '__main__':
    matrix = []
    with open('2024/data/8.txt', 'rt') as file:
        for row in file:
            matrix.append(list(row.strip()))

    antenas = find_antennas(matrix)
    find_antinodes(antenas)
