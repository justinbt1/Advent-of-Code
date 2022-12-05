
def parse_assignment_data():
    elf_section_assignments = []

    with open('data/4.txt', 'rt') as data_file:
        for line in data_file:
            assingment = line.strip().split(',')
            x1, x2 = [int(section) for section in assingment[0].split('-')]
            y1, y2 = [int(section) for section in assingment[1].split('-')]
            x_range = set(i for i in range(x1, x2 + 1))
            y_range = set(i for i in range(y1, y2 + 1))
            elf_section_assignments.append((x_range, y_range))

    return elf_section_assignments


def part_1(assignments):
    subset_count = 0
    for assingment in assignments:
        if assingment[0].issubset(assingment[1]):
            subset_count += 1
        elif assingment[1].issubset(assingment[0]):
            subset_count += 1

        print(subset_count, assingment)

    print(subset_count)


def part_2(assignments):
    ovelaps_count = 0
    for assingment in assignments:
        if assingment[0].intersection(assingment[1]):
            ovelaps_count += 1

    print(ovelaps_count)


if __name__ == '__main__':
    elf_assignments = parse_assignment_data()
    part_1(elf_assignments)
    part_2(elf_assignments)
