import numpy as np


class Location:
    def __init__(self):
        self.coords = np.array((0, 0))
        self._i = 0

    def re_orient(self, turn):
        orientations = np.array([(0, -1), (-1, 0), (0, 1), (1, 0)])
        i = 3 if turn == 'L' else 1
        self._i = (self._i + i) % 4

        return orientations[self._i]

    def walk(self, direction):
        orientation = self.re_orient(direction[0])
        new_location = orientation * int(direction[1])
        self.coords += new_location

    def get_distance(self):
        print(np.abs(self.coords).sum())


def find_bunny_hq(instructions):
    location = Location()
    for instruction in instructions:
        location.walk(instruction)

    location.get_distance()


if __name__ == '__main__':
    with open('2016/data/1.txt', 'rt') as file:
        instructions = file.read().strip().split(', ')
        instructions = [list(d) for d in instructions]

    find_bunny_hq(instructions)
