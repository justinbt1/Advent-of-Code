def get_stack_data(file_buffer):
    stacks = []
    for line in file_buffer:
        if not line.strip():
            break
        stacks.append(list(line))

    return stacks


def create_stack_dict(stacks):
    stack_names = stacks[-1]
    i = 0
    stack_dict = {}
    for stack in stack_names:
        if stack.strip():
            stack_dict[stack] = []
            for row in stacks[:-1]:
                if row[i].strip():
                    stack_dict[stack].append(row[i])
        i += 1

    return stack_dict


def get_procedures(file_buffer):
    procedures = []
    for line in file_buffer:
        line = line.split()
        procedures.append((int(line[1]), line[3], line[5]))

    return procedures


def rearrange_crates(stacks, procedures):
    for procedure in procedures:
        for _ in range(procedure[0]):
            crate = stacks[procedure[1]].pop(0)
            stacks[procedure[2]].insert(0, crate)

    return stacks


def rearrange_inorder(stacks, procedures):
    for procedure in procedures:
        new_stack = stacks[procedure[1]][:procedure[0]] + stacks[procedure[2]]
        stacks[procedure[2]] = new_stack
        stacks[procedure[1]] = stacks[procedure[1]][procedure[0]:]

    return stacks


def elf_message(stacks):
    message = ''
    for i in stacks:
        message += stacks[i][0]

    print(message)


def part_1(stack_data, procedures):
    stack_dict = create_stack_dict(stack_data)
    rearranged_stacks = rearrange_crates(stack_dict, procedures)
    elf_message(rearranged_stacks)


def part_2(stack_data, procedures):
    stack_dict = create_stack_dict(stack_data)
    rearranged_stacks = rearrange_inorder(stack_dict, procedures)
    elf_message(rearranged_stacks)


if __name__ == '__main__':
    with open('data/5.txt', 'rt') as input_file:
        stack_data = get_stack_data(input_file)
        procedures = get_procedures(input_file)

    part_1(stack_data, procedures)
    part_2(stack_data, procedures)
