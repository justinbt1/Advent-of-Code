with open('2025/data/7.txt', 'rt') as tachyon_buffer:
    tachyon_manifold = [list(row) for row in tachyon_buffer.read().splitlines()]

visited = set()


def traverse_manifold(m, n, manifold):
    while True:
        if m == len(manifold):
            return
        if manifold[m][n] == '^':
            if tuple([m, n]) in visited:
                return
            break
        else:
            m += 1
    
    visited.add(tuple([m, n]))
    traverse_manifold(m, n - 1, manifold)
    traverse_manifold(m, n + 1, manifold)


def part_one():
    initial_n = tachyon_manifold[0].index('S')
    traverse_manifold(0, initial_n, tachyon_manifold)
    print(len(visited))
