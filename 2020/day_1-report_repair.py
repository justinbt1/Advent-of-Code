def part_one(expenses):
    for value in expenses:
        for expense in expenses:
            if value + expense == 2020:
                return value * expense
            
def part_two(expenses):
    for value1 in expenses:
        for value2 in expenses:
            for value3 in expenses:
                if value3 + value2 + value1 == 2020:
                    return value3 * value2 * value1


if __name__ == '__main__':
    with open('2020/data/1.txt', 'rt') as file:
        lines = [int(line.strip()) for line in file]

    print(part_one(lines))
    print(part_two(lines))  
