
def captcha_solver(digits, step=1):
    total = 0
    n_digits = len(digits)
    for i in range(0, n_digits):
        j = (i + step) % n_digits
        if digits[i] == digits[j]:
            total += digits[i]

    print(total)


if __name__ == '__main__':
    with open('2017/data/1.txt', 'rt') as file:
        line = file.read().strip()
        digits = [int(digit.strip()) for digit in line]

        captcha_solver(digits)
        captcha_solver(digits, step=int(len(digits) / 2))
