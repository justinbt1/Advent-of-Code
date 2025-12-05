

def read_data():
    ranges = []
    ids = []
    with open('2025/data/5.txt', 'rt') as input_buffer:
        range_mode = True
        for row in input_buffer:
            if not row.strip():
                range_mode = False
                continue

            if range_mode:
                ranges.append([int(n) for n in row.strip().split('-')])
            else:
                ids.append(int(row.strip()))

    return ranges, ids


def merge_ranges(ranges):
    merged_ranges = []
    while True:
        if not ranges:
            break

        r = ranges.pop(0)
        overlap = False
        for i, v in enumerate(ranges):
            if r[0] <= v[0] -1 <= r[1]:
                ranges[i][0] = r[0]
                overlap = True
            if r[1] >= v[1] + 1 >= r[0]:
                ranges[i][1] = r[1]
                overlap = True
            if r[0] <= v[0] and r[1] >= v[1]:
                ranges[i] = r
                overlap = True
            if r[0] >= v[0] and r[1] <= v[1]:
                overlap = True
        
        if not overlap:
            merged_ranges.append(r)

    return merged_ranges


def part_one(ranges, ids):
    fresh_count = 0
    for i in ids:
        for r in ranges:
            if r[0] <= i <= r[1]:
                fresh_count += 1
                break

    print(fresh_count)


def part_two(ranges):
    total_fresh_values = 0
    for pair in ranges:
        total_fresh_values += pair[1] - pair[0] + 1

    print(total_fresh_values)


if __name__ == '__main__':
    ranges, ids = read_data()
    ranges = merge_ranges(ranges)
    part_one(ranges, ids)
    part_two(ranges)
