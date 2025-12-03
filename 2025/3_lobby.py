def read_data():
    banks = []
    with open('2025/data/3.txt', 'rt') as battery_buffer:
        for bank in battery_buffer:
            banks.append([int(battery) for battery in bank.strip()])

    return banks


def find_highest(bank, n, i):
    if n - i == 1:
        return str(max(bank))
    max_i = bank[:-n + i + 1].index(max(bank[:-n + i + 1]))
    return str(bank[max_i]) + find_highest(bank[max_i + 1:], n, i + 1)


def find_total_joltage(data, n):
    total = 0
    for bank in data:
        total += int(find_highest(bank, n=n, i=0))
    
    print(total)


if __name__ == '__main__':
    data = read_data()

    find_total_joltage(data, n=2)
    find_total_joltage(data, n=12)
