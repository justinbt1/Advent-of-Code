def read_data():
    banks = []
    with open('2025/data/3.txt', 'rt') as battery_buffer:
        for bank in battery_buffer:
            banks.append([int(battery) for battery in bank.strip()])

    return banks


def find_highest(bank, n, i):
    if n - i == 1:
        return str(max(bank)), []
    max_i = bank[:-n + i + 1].index(max(bank[:-n + i + 1]))
    return str(bank[max_i]), bank[max_i + 1:]


def find_total_joltage(data, n):
    output_joltages = []
    for bank in data:
        max_joltage = ''
        i = 0
        while True:
            joltage, bank = find_highest(bank, n=n, i=i)
            max_joltage += joltage
            i += 1
            if len(max_joltage) == n:
                break
        output_joltages.append(int(max_joltage))
    
    print(sum(output_joltages))
    

if __name__ == '__main__':
    data = read_data()

    find_total_joltage(data, n=2)
    find_total_joltage(data, n=12)
