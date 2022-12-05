import string


def priorities():
    chars = string.ascii_lowercase + string.ascii_uppercase
    char_priorities = {char: i + 1 for i, char in enumerate(chars)}

    return char_priorities


def part_1(rucksack_items, priority_ref):
    total_priority = 0

    for items in rucksack_items:
        n_items = int(len(items) / 2)
        rucksack_1 = set(items[:n_items])
        rucksack_2 = set(items[n_items:])
        repeat_char = rucksack_1 & rucksack_2
        total_priority += priority_ref[repeat_char.pop()]

    print(total_priority)


def part_2(rucksack_items, priority_ref):
    total_priority = 0

    for i in range(0, len(rucksack_items), 3):
        group_rucksacks = [set(rucksack)for rucksack in rucksack_items[i:i+3]]
        badge = set.intersection(*group_rucksacks)
        total_priority += priority_ref[badge.pop()]

    print(total_priority)


if __name__ == '__main__':
    with open('data/3.txt', 'rt') as data_file:
        rucksacks = [list(line.strip()) for line in data_file]

    priorities_lookup = priorities()

    part_1(rucksacks, priorities_lookup)
    part_2(rucksacks, priorities_lookup)
