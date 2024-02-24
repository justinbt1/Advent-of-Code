from itertools import cycle


def part_one(frequency_changes):
    current_frequency = 0
    for change in frequency_changes:
        current_frequency += change
        
    print(current_frequency)


def part_two(frequency_changes):
    previous_frequencies = {0}
    current_frequency = 0
    for change in cycle(frequency_changes):
        current_frequency += change
        
        if current_frequency in previous_frequencies:
            print(current_frequency)
            break
            
        previous_frequencies.add(current_frequency)


if __name__ == '__main__':
    with open('2018/data/1.txt', 'rt') as file:
        frequencies = [int(line.strip()) for line in file]

    part_one(frequencies)
    part_two(frequencies)
