def load_data():
    tests = []
    with open('2024/data/7.txt') as file:
        for row in file:
            test_value, equation = row.split(':')
            equation_values = [int(n) for n in equation.strip().split()]
            tests.append(((int(test_value), equation_values)))

    return tests


def find_operators(value, all_values, test, concat, i=1):
    if i < len(all_values):
        add = value + all_values[i]
        valid_add = find_operators(add, all_values, test, concat, i=i+1)
        mul = value * all_values[i]
        valid_mul = find_operators(mul, all_values, test, concat, i=i+1)
        valid_concat = None
        if concat:
            con = int(str(value) + str(all_values[i]))
            valid_concat = find_operators(con, all_values, test, concat, i=i+1)
        if valid_add or valid_mul or valid_concat:
            return True
    else:
        if value == test:
            return True


def validate_calibrations(data, concat=False):
    total_calibration_result = 0
    for test, values in data:
        valid = find_operators(values[0], values, test, concat)
        if valid:
            total_calibration_result += test

    print(total_calibration_result)


if __name__ == '__main__':
    test_data = load_data()
    validate_calibrations(test_data)
    validate_calibrations(test_data, concat=True)
