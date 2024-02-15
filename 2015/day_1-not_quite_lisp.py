def move_floor(command):
    if command == '(':
        return 1
    else:
        return -1


def what_floor(instructions):
    floor = 0
    for instruction in instructions:
        floor += move_floor(instruction)

    print(floor)

def when_basement(instructions):
    floor = 0
    for i, instruction in enumerate(instructions):
        floor += move_floor(instruction)
        if floor < 0:
            break

    print(i)


if __name__ == '__main__':
    floor = 0
    with open('2015/data/1.txt', 'rt') as input_file:
        data = input_file.read().strip()
        what_floor(data)
        when_basement(data)

