import json


class Monkey:
    pass


if __name__ == "__main__":
    with open('data/10.txt', 'rt') as input_file:
        monkey_data = json.load(input_file)

    print(monkey_data['Monkey 0'])
