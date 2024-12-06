import numpy as np


class Gaurd:
    def __init__(self, start_position):
        self.facing = 0
        self.position = start_position
        self.directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]

    def move(self):
        while True:
            next_position = [
                x + y for x, y in zip(self.position, self.directions[self.facing])
            ]
            if lab_map[next_position[0], next_position[1]] == '#':
                self.facing = (self.facing + 1) % 4
            else:
                lab_map[next_position[0], next_position[1]] = 'X'
                self.position = next_position
                break


def part_one():
    m, n = np.where(lab_map == '^')
    gaurd = Gaurd([m[0], n[0]])
    visited = [tuple([m[0], n[0]])]
    while True:
        try:
            gaurd.move()
            visited.append(tuple(gaurd.position))
        except IndexError:
            break
    
    for m in lab_map:
        print(''.join(m.tolist()))

    print(len(set(visited)))


if __name__ == '__main__':
    with open('2024/data/6.txt', 'rt') as file:
        lab_map = np.array([list(row.strip()) for row in file])

    part_one()
