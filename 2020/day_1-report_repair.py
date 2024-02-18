def part_one(expenses):
    for value in expenses:
        for expense in expenses:
            if value + expense == 2020:
                return value * expense


if __name__ == '__main__':
    with open('2020/data/1.txt', 'rt') as file:
        lines = [int(line.strip()) for line in file]

    print(part_one(lines))
