
class Monkey:
    def __init__(self):
        self.items = None
        self.operation = None
        self.test = None
        self.if_true = None
        self.if_false = None
        self.inspection_count = 0

    def inspect_item(self):
        self.inspection_count += 1
        item = self.items.pop(0)
        if self.operation[0] == '*':
            if self.operation[-1] == 'old':
                item = int(item) * int(item)
            else:
                item = int(item) * int(self.operation[-1])
        else:
            if self.operation[-1] == 'old':
                item = int(item) * int(item)
            else:
                item = int(item) + int(self.operation[-1])
        return item

    def next_monkey(self, item):
        if not int(item) % int(self.test):
            return int(self.if_true)
        else:
            return int(self.if_false)


def conduct_rounds(monkeys, n, relief=True):
    for i in range(n):
        print(f'Round: {i}')
        for monkey in monkeys:
            for _ in range(len(monkey.items)):
                item = monkey.inspect_item()
                if relief:
                    item = item // 3
                next_monkey = monkey.next_monkey(item)
                monkeys[next_monkey].items.append(item)

    return monkeys


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
            case ['Test:', *test]:
                monkey.test = test[-1]
            case ['If', 'true:', *recieving_monkey]:
                monkey.if_true = recieving_monkey[-1]
            case ['If', 'false:', *recieving_monkey]:
                monkey.if_false = recieving_monkey[-1]

    monkeys.append(monkey)

    return monkeys


def find_top_monkey_business(monkey_data, n_rounds, relief=False):
    monkeys = conduct_rounds(monkey_data, n_rounds, relief=relief)

    inspections = []
    for monkey in monkeys:
        inspections.append(monkey.inspection_count)

    inspections.sort()
    monkey_business = inspections[-2] * inspections[-1]
    print(monkey_business)


if __name__ == "__main__":
    with open('data/11.txt', 'rt') as input_file:
        monkey_data = read_data(input_file)
        find_top_monkey_business(monkey_data, 20, True)
        # find_top_monkey_business(monkey_data, 1000, False)
