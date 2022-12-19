def read_motions():
    with open('data/9.txt', 'rt') as input_file:
        motions = []
        for motion in input_file:
            motion_details = motion.strip().split()
            motions.append((motion_details[0], int(motion_details[1])))

    return motions


def shift_knots(rope):
    for i in range(len(rope) - 1):
        previous = rope[i]
        current = rope[i + 1]

        if (previous[0] - current[0]) > 1:
            current[0] += 1
            current[1] = previous[1]

        elif (current[0] - previous[0]) > 1:
            current[0] -= 1
            current[1] = previous[1]

        elif (previous[1] - current[1]) > 1:
            current[1] += 1
            current[0] = previous[0]

        elif (current[1] - previous[1]) > 1:
            current[1] -= 1
            current[0] = previous[0]

    return rope


def test(n):
    tracker = [(0, 0)]
    rope = [[0, 0] for i in range(n)]
    motions = read_motions()

    for motion in motions:
        if motion[0] == 'R':
            for _ in range(motion[1]):
                rope[0][0] += 1
                rope = shift_knots(rope)
                tracker.append(tuple(rope[-1]))

        elif motion[0] == 'L':
            for _ in range(motion[1]):
                rope[0][0] -= 1
                rope = shift_knots(rope)
                tracker.append(tuple(rope[-1]))

        elif motion[0] == 'U':
            for _ in range(motion[1]):
                rope[0][1] += 1
                rope = shift_knots(rope)
                tracker.append(tuple(rope[-1]))

        elif motion[0] == 'D':
            for _ in range(motion[1]):
                rope[0][1] -= 1
                rope = shift_knots(rope)
                tracker.append(tuple(rope[-1]))

    return len(set(tracker))


if __name__ == '__main__':
    tail_visits = test(2)
    print(f'Part 1: {tail_visits}')
    tail_visits = test(10)
    print(f'Part 2: {tail_visits}')
