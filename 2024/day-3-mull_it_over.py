import re


def remove_invalid_chunks(text):
    while True:
        do_not = text.find('don\'t()')
        if do_not == -1:
            break

        do = text.find('do()')
        if do > do_not:
            text = text[:do_not] + text[do:]
        else:
            text = text[:do] + text[do + 4:]

    return text


def extract_valid_operations(text):
    operators = re.findall(r'mul\([0-9]{1,3},[0-9]{1,3}\)', text)
    values = [op[4:-1].split(',') for op in operators]
    sum_products = sum([int(x) * int(y) for x, y in values])

    return sum_products


if __name__ == '__main__':
    with open('2024/data/3.txt', 'rt') as file:
        text = file.read()

    part_one = extract_valid_operations(text)
    print(part_one)

    valid_text = remove_invalid_chunks(text)
    part_two = extract_valid_operations(valid_text)
    print(part_two)
