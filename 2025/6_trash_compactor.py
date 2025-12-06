import math


def load_data():
    with open('2025/data/6.txt', 'rt') as buffer:
        data = buffer.read().splitlines()

    operators_i = [i for i, j in enumerate(data[-1]) if j != ' '] + [len(data[0])]
    op_map = {'*': math.prod, '+': sum}
    operators = [op_map[op] for op in data[-1].split()]

    number_array = []
    for i, j in zip(operators_i[:-1], operators_i[1:]):
        number_array.append([row[i:j] for row in data[:-1]])

    return number_array, operators


def part_one(number_rows, operators):
    grand_total = 0
    for row, op in zip(number_rows, operators):
        grand_total += op([int(n) for n in row])

    print(grand_total)


def part_two(number_rows, operators):
    grand_total = 0
    for row, op in zip(number_rows, operators):
        recombined = []
        for i in range(len(row[0]) - 1, 0 - 1, -1):
            recombined_number = ''
            for number in row:
                recombined_number += number[i]
            if recombined_number.strip():
                recombined.append(int(recombined_number))
        grand_total += op(recombined)
    print(grand_total)
        

if __name__ == '__main__':
    number_rows, operators = load_data()
    part_one(number_rows, operators)
    part_two(number_rows, operators)
