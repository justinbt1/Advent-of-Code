
def what_floor(instructions):
    floor = 0
    for instruction in instructions:
        if instruction == '(':
            floor += 1
        else:
            floor -= 1

    print(floor)



if __name__ == '__main__':
    with open('2015/data/1.txt', 'rt') as input_file:
        data = input_file.read().strip()
        print(data)
        what_floor(data)
