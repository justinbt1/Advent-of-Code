
def get_instructions():
    with open('data/10.txt', 'rt') as input_file:
        instructions = [line.strip() for line in input_file]

    return instructions


class AddX:
    def __init__(self, instruction):
        self.remaining_cycles = 1
        self.value = int(instruction[1])


if __name__ == '__main__':
    with open('data/10.txt', 'rt') as input_file:
        instructions = [line.strip().split() for line in input_file]

    register = 1
    clock_cycle = 1
    next_cycle = 20
    current_operation = None
    next_instruction = 0
    signal_strengths = 0

    while True:
        clock_cycle += 1
        if current_operation:
            if current_operation.remaining_cycles > 1:
                current_operation.remaining_cycles -= 1
            else:
                register += current_operation.value
                current_operation = None
        else:
            if next_instruction == len(instructions):
                break

            current_instruction = instructions[next_instruction]
            if current_instruction[0] == 'addx':
                current_operation = AddX(current_instruction)
            next_instruction += 1

        if clock_cycle == next_cycle:
            signal_strengths += clock_cycle * register
            next_cycle += 40
            print(clock_cycle, register)

    print(signal_strengths)
