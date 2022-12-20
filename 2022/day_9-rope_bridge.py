def read_motions():
    with open('data/9.txt', 'rt') as input_file:
        motions = []
        for motion in input_file:
            motion_details = motion.strip().split()
            motions.append((motion_details[0], int(motion_details[1])))

    return motions


def shift_knots(current, previous, axis):
    current[axis] += int((previous[axis] - current[axis]) / 2)
    if previous[1 - axis] > current[1 - axis]:
        current[1 - axis] += 1
    elif previous[1 - axis] < current[1 - axis]:
        current[1 - axis] -= 1


def simulate_rope(rope):
    for i in range(len(rope) - 1):
        previous = rope[i]
        current = rope[i + 1]

        if abs(previous[0] - current[0]) == 2:
            shift_knots(current, previous, 0)
        elif abs(previous[1] - current[1]) == 2:
            shift_knots(current, previous, 1)

    return rope


def go_through_the_motions(rope, axis, direction, distance, tracker):
    step = 1 * direction
    for _ in range(distance):
        rope[0][axis] += step
        rope = simulate_rope(rope)
        tracker.append(tuple(rope[-1]))


def model_rope_bridge(n):
    tracker = [(0, 0)]
    rope = [[0, 0] for i in range(n)]
    motions = read_motions()

    for motion in motions:
        if motion[0] == 'R':
            go_through_the_motions(rope, 0, 1, motion[1], tracker)
        elif motion[0] == 'L':
            go_through_the_motions(rope, 0, -1, motion[1], tracker)
        elif motion[0] == 'U':
            go_through_the_motions(rope, 1, 1, motion[1], tracker)
        elif motion[0] == 'D':
            go_through_the_motions(rope, 1, -1, motion[1], tracker)

    return len(set(tracker))


if __name__ == '__main__':
    tail_visits = model_rope_bridge(2)
    print(f'Part 1: {tail_visits}')
    tail_visits = model_rope_bridge(10)
    print(f'Part 2: {tail_visits}')
