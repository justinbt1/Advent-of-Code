
def part_one(frequency_changes):
    current_frequency = 0
    for change in frequency_changes:
        current_frequency += change
        
    print(current_frequency)


if __name__ == '__main__':
    with open('2018/data/1.txt', 'rt') as file:
        frequencies = [int(line.strip()) for line in file]

    part_one(frequencies)
