

class BunnyHQSearch:
    def __init__(self, instructions, track=False):
        self._i = 0
        self.position = (0, 0)
        self.coords = set((0, 0))
        self.track = track
        self.test = [(0, 0)]
        self.search(instructions)

    def re_orient(self, turn):
        compass = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        self._i = (self._i + (3 if turn == 'L' else 1)) % 4
        return compass[self._i]

    def walk(self, direction, steps):
        increment = self.re_orient(direction)
        for _ in range(steps):
            self.position = tuple(map(sum, zip(self.position, increment)))
            self.test.append(self.position)
            if self.track:
                if self.position in self.coords:
                    print(self.position)
                    return
                self.coords.add(self.position)

    def search(self, instructions):
        for direction, steps in instructions:
            self.walk(direction, steps)
        
        print(self.position)
        print(sum([abs(l) for l in self.position]))

        tracker = set(self.test[0])
        for pos in self.test[1:]:
            if pos in tracker:
                print(pos)
                break
            tracker.add(pos)


if __name__ == '__main__':
    with open('2016/data/1.txt', 'rt') as file:
        instructions = [(line[0], int(line[1:])) for line in file.read().split(', ')]

    # BunnyHQSearch(instructions)
    BunnyHQSearch(instructions, track=True)
