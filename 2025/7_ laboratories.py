
visit_log = {}
vl = {}


def traverse_manifold(m, n, manifold):
    """Count number of ^splitters """
    while True:
        if m == len(manifold) - 1:
            return
        if manifold[m][n] == '^':
            if visit_log.get(tuple([m, n])):
                visit_log[tuple([m, n])] += 1
                return
            visit_log[tuple([m, n])] = 1
            break
        else:
            m += 1
    
    traverse_manifold(m, n - 1, manifold)
    traverse_manifold(m, n + 1, manifold)


def traverse_quantum_manifold(m, n, manifold):
    """Count number of paths """
    while True:
        if vl.get(tuple([m, n])):
            return 0
        if m == len(manifold) - 1:
            return 0
        if manifold[m][n] == '^':
            left = traverse_quantum_manifold(m, n - 1, manifold)
            right = traverse_quantum_manifold(m, n + 1, manifold)
            if visit_log.get(tuple([m, n])) > 1:
                left = left * visit_log[tuple([m, n])]
                right = right * visit_log[tuple([m, n])]
                count = left + right
                if count == 0:
                    count = 2
            else:
                count = 2 + left + right
                if count == 0:
                    count = 2
            vl[tuple([m, n])] = count
            return count
        else:
            m += 1

    
def part_one():
    with open('2025/data/7.txt', 'rt') as tachyon_buffer:
        tachyon_manifold = [list(row) for row in tachyon_buffer.read().splitlines()]
    initial_n = tachyon_manifold[0].index('S')
    traverse_manifold(0, initial_n, tachyon_manifold)
    print(len(visit_log))

    print(traverse_quantum_manifold(0, initial_n, tachyon_manifold))

    for k, v in vl.items():
        m, n = k
        tachyon_manifold[m][n] = str(v)

    for r in tachyon_manifold:
        print(''.join(r))


if __name__ == "__main__":
    part_one()
