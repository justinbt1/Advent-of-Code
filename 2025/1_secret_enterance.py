
def read_rotations():
    rotations = []
    with open('2025/data/1.txt', 'rt') as rotation_buffer:
        for instruction in rotation_buffer:
            rotation = int(instruction[1:])
            if instruction[0] == 'L':
                rotation = -rotation

            rotations.append(rotation)

    return rotations


def zero_count(rotations, dial_max=99):
    dial_position = 50
    zero_count = 0
    for r in rotations:
        dial_position = (dial_position + r) % (dial_max + 1)
        if dial_position == 0:
            zero_count += 1

    print(zero_count)


def zero_point_count(rotations, dial_max=99):
    dial_position = 50
    zero_count = 0
    for rotation in rotations:
        for r in range(0, rotation, -1):
            dial_position = (dial_position + r) % (dial_max + 1)
            print(dial_position)

        break

    print(zero_count)


if __name__ == '__main__':
    rotations = read_rotations()
    # zero_count(rotations)
    zero_point_count(rotations)
