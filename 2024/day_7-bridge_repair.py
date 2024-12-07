def load_data():
    tests = []
    with open('2024/data/7.txt') as file:
        for row in file:
            test_value, equation = row.split(':')
            equation_values = [int(n) for n in equation.strip().split()]
            tests.append(((int(test_value), equation_values)))

    return tests


def find_operators(value, all_values, test, i=1):
    if i < len(all_values):
        add = value + all_values[i]
        valid_add = find_operators(add, all_values, test, i=i+1)
        mul = value * all_values[i]
        valid_mul = find_operators(mul, all_values, test, i=i+1)
        if valid_add or valid_mul:
            return True
    else:
        if value == test:
            return True


def part_one(data):
    total_calibration_result = 0
    for test_value, equation_values in data:
        valid = find_operators(equation_values[0], equation_values, test_value)
        if valid:
            total_calibration_result += test_value

    print(total_calibration_result)


if __name__ == '__main__':
    test_data = load_data()
    part_one(test_data)
