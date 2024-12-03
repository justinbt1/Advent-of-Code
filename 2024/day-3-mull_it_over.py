import re

def extract_valid_operations(text):
    operators = re.findall(r'mul\([0-9]{1,3},[0-9]{1,3}\)', text)
    values = [op[4:-1].split(',') for op in operators]
    products = [int(x) * int(y) for x, y in values]
    total = sum(products)

    return total


if __name__ == '__main__':
    with open('2024/data/3.txt', 'rt') as file:
        text = file.read()

    muls = extract_valid_operations(text)
    print(muls)
