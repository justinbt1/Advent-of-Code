import math


class Monkey:
    def __init__(self):
        self.items = None
        self.operation = None
        self.divisor = None
        self.if_true = None
        self.if_false = None
        self.inspection_count = 0

    def inspect_item(self, mod):
        self.inspection_count += 1
        item = int(self.items.pop(0)) % mod
        if self.operation[0] == '*':
            if self.operation[-1] == 'old':
                item = item * item
            else:
                item = item * int(self.operation[-1])
        else:
            if self.operation[-1] == 'old':
                item = item * item
            else:
                item = item + int(self.operation[-1])
        return item

    def next_monkey(self, item):
        if not item % int(self.divisor):
            return int(self.if_true)
        else:
            return int(self.if_false)


def read_data(data_file):
    monkeys = []
    monkey = Monkey()
    for line in data_file:
        line = line.strip()
        if not line:
            monkeys.append(monkey)
            monkey = Monkey()

        match line.split():
            case ['Starting', 'items:', *items]:
                monkey.items = [item.replace(',', '') for item in items]
            case ['Operation:', *operation]:
                monkey.operation = operation[-2:]
            case ['Test:', *divisor]:
                monkey.divisor = divisor[-1]
            case ['If', 'true:', *recieving_monkey]:
                monkey.if_true = recieving_monkey[-1]
            case ['If', 'false:', *recieving_monkey]:
                monkey.if_false = recieving_monkey[-1]

    monkeys.append(monkey)

    return monkeys


def conduct_rounds(monkeys, n, part):
    modulus = math.lcm(*[int(monkey.divisor) for monkey in monkeys])
    for i in range(n):
        for monkey in monkeys:
            for _ in range(len(monkey.items)):
                item = monkey.inspect_item(modulus)
                if part == 1:
                    item = item // 3
                next_monkey = monkey.next_monkey(item)
                monkeys[next_monkey].items.append(item)

        if i + 1 in [1, 20, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]:
            print(f'Round: {i}')
            l = []
            for j, monkey in enumerate(monkeys):
                l.append(monkey.inspection_count)
            print(l)

    return monkeys


def find_top_monkey_business(monkey_data, n_rounds, part):
    monkeys = conduct_rounds(monkey_data, n_rounds, part=part)
    inspections = sorted([monkey.inspection_count for monkey in monkeys])
    monkey_business = inspections[-2] * inspections[-1]
    print(monkey_business)


if __name__ == "__main__":
    with open('data/11.txt', 'rt') as input_file:
        monkey_data = read_data(input_file)
        find_top_monkey_business(monkey_data, 20, part=1)
        find_top_monkey_business(monkey_data, 10000, part=2)
