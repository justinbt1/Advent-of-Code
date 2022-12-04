import string


def part_1(rucksack_items):
    chars = string.ascii_lowercase + string.ascii_uppercase
    char_priorities = {char: i + 1 for i, char in enumerate(chars)}
    total_priority = 0

    for items in rucksack_items:
        n_items = int(len(items) / 2)
        rucksack_1 = set(items[:n_items])
        rucksack_2 = set(items[n_items:])
        repeat_char = rucksack_1 & rucksack_2
        priority = char_priorities[repeat_char.pop()]
        total_priority += priority

    print(total_priority)


if __name__ == '__main__':
    with open('data/3.txt', 'rt') as data_file:
        rucksacks = [list(line.strip()) for line in data_file]

    part_1(rucksacks)
