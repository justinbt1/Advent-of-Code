key_pad = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

steps = {'U': (0, -1), 'D': (0, 1), 'L': (1, -1), 'R': (1, 1)}

def get_code(instructions):
    position = [1, 1]
    for directions in instructions:
        for direction in directions:
            i, n = steps[direction]
            position[i] += n
            y, x = position
            print(key_pad[y][x])
        print()
            


if __name__ == '__main__':
    with open('2016/data/2.txt', 'rt') as file:
        data = [list(line.strip()) for line in file]
    
    get_code(data)
