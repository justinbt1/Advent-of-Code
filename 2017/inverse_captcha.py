def part_one(digits):
    total = 0
    n_digits = len(digits)
    for i in range(0, n_digits):
        j = (i + 1) % n_digits
        if digits[i] == digits[j]:
            total += digits[i]

    print(total)


if __name__ == '__main__':
    with open('2017/data/1.txt', 'rt') as file:
        line = file.read().strip()
        digits = [int(digit.strip()) for digit in line]

        part_one(digits)
