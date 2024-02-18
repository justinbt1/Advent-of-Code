
def part_one(lines):
    callibration_sum = 0
    for line in lines:
        digits = [char for char in line if char.isdigit()]
        callibration_sum += int(digits[0] + digits[-1])

    print(callibration_sum)


def get_digit(line, look_up, start, stop, step):
    for i in range(start, stop, step):
        if line[i].isdigit():
            return line[i]
        else:
            for number in look_up.keys():
                if line[i:i + len(number)] == number:
                    return look_up[number]


def part_two(lines):
    look_up = {
        'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5',
        'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'
    }

    callibration_sum = 0
    for line in lines:
        digit = ''
        digit += get_digit(line, look_up, 0, len(line), 1)
        digit += get_digit(line, look_up, len(line) - 1, -1, -1)
        print(digit)
        
        callibration_sum += int(digit)
    
    print(callibration_sum)


if __name__ == '__main__':
    file = open('2023/data/1.txt', 'rt')
    file_lines = [line.strip() for line in file]
    file.close()

    part_two(file_lines)
