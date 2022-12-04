
def part_1(rucksack_items):
    for items in rucksack_items:
        n_items = int(len(items) / 2)
        rucksack_1 = set(items[:n_items])
        rucksack_2 = set(items[n_items:])
        repeat_char = rucksack_1 & rucksack_2
        print(repeat_char)
        print(ord(repeat_char.pop()))



if __name__ == '__main__':
    with open('data/3.txt', 'rt') as data_file:
        rucksacks = [list(line.strip()) for line in data_file]

    part_1(rucksacks)
