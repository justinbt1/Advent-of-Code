

if __name__ == '__main__':
    tracker = [(0, 0)]
    head_x = 0
    head_y = 0
    tail_x = 0
    tail_y = 0

    with open('data/9.txt', 'rt') as input_file:
        motions = []
        for motion in input_file:
            motion_details = motion.strip().split()
            motions.append((motion_details[0], int(motion_details[1])))

    for motion in motions:
        if motion[0] == 'R':
            for i in range(motion[1]):
                head_x += 1
                if (head_x - tail_x) > 1:
                    tail_x += 1
                    tail_y = head_y
                    tracker.append((tail_x, tail_y))

        elif motion[0] == 'L':
            for i in range(motion[1]):
                head_x -= 1
                if (tail_x - head_x) > 1:
                    tail_x -= 1
                    tail_y = head_y
                    tracker.append((tail_x, tail_y))

        elif motion[0] == 'U':
            for i in range(motion[1]):
                head_y += 1
                if (head_y - tail_y) > 1:
                    tail_y += 1
                    tail_x = head_x
                    tracker.append((tail_x, tail_y))

        elif motion[0] == 'D':
            for i in range(motion[1]):
                head_y -= 1
                if (tail_y - head_y) > 1:
                    tail_y -= 1
                    tail_x = head_x
                    tracker.append((tail_x, tail_y))

        print(motion, head_x, head_y, tail_x, tail_y)

    print(f'Part 1: {len(set(tracker))}')
