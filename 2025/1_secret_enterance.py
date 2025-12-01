
def read_rotations():
    with open('2025/data/1.txt', 'rt') as rotation_buffer:
    
        return [(int(i[1:]), i[0]) for i in rotation_buffer]


def zero_count(instructions, dial_max=99, dial_position=50):
    zero_count = 0
    for distance, direction in instructions:
        i = -distance if direction == 'L' else distance
        dial_position = (dial_position + i) % (dial_max + 1)
        if dial_position == 0:
            zero_count += 1

    print(zero_count)


def zero_point_count(instructions, dial_max=99, dial_position=50):
    zero_count = 0
    for distance, direction in instructions:
        for _ in range(distance):
            i = -1 if direction == 'L' else 1
            dial_position = (dial_position + i) % (dial_max + 1)
            if dial_position == 0:
                zero_count += 1
    
    print(zero_count)


if __name__ == '__main__':
    rotations = read_rotations()
    zero_count(rotations)
    zero_point_count(rotations)
