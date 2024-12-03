import re


def remove_invalid_chunks(text):

    a = text
    while True:
        do_not = a.find('don\'t()')
        if do_not == -1:
            break

        do = a.find('do()')

        if do > do_not:
            a = a[:do_not] + a[do:]
        else:
            a = a[:do] + a[do + 4:]

    return a


def extract_valid_operations(text):
    operators = re.findall(r'mul\([0-9]{1,3},[0-9]{1,3}\)', text)
    values = [op[4:-1].split(',') for op in operators]
    products = [int(x) * int(y) for x, y in values]
    total = sum(products)

    return total


if __name__ == '__main__':
    with open('2024/data/3.txt', 'rt') as file:
        text = file.read()

    part_one = extract_valid_operations(text)
    print(part_one)

    part_two = remove_invalid_chunks(text)
    part_two = extract_valid_operations(part_two)
    print(part_two)
