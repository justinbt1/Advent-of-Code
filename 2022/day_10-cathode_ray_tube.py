
def get_instructions():
    with open('data/10.txt', 'rt') as input_file:
        instructions = [line.strip().split() for line in input_file]

    return instructions


def print_pixel(clock_cycle, register):
    pixel = '.'
    pixel_pos = (clock_cycle) % 40
    if pixel_pos - 1 in (register - 1, register, register + 1):
        pixel = '#'

    if pixel_pos == 0:
        pixel += '\n'

    return pixel


def run_instructions():
    instructions = get_instructions()
    register = 1
    clock_cycle = 1
    next_cycle = 20
    current_operation = None
    next_instruction = 0
    signal_strengths = 0
    output = '#'

    while True:
        clock_cycle += 1
        if current_operation:
            register += current_operation
            current_operation = None
        else:
            if next_instruction == len(instructions):
                break

            current_instruction = instructions[next_instruction]
            if current_instruction[0] == 'addx':
                current_operation = int(current_instruction[1])
            next_instruction += 1

        if clock_cycle == next_cycle:
            signal_strengths += clock_cycle * register
            next_cycle += 40

        output += print_pixel(clock_cycle, register)
    print(signal_strengths)
    print(output)


if __name__ == '__main__':
    run_instructions()
