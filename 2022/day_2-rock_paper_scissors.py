

def part_1(data):
    total_score = 0
    plays_as_ints = {'A': 1, 'B': 2, 'C': 3, 'X': 1, 'Y': 2, 'Z': 3}
    for line in data:
        opponent = plays_as_ints[line[0]]
        response = plays_as_ints[line[1]]
        total_score += response

        if opponent == response:
            total_score += 3
        elif opponent + 1 == response:
            total_score += 6
        elif opponent - 2 == response:
            total_score += 6

    print(total_score)


def part_2(data):
    total_score = 0
    plays_as_ints = {'A': 1, 'B': 2, 'C': 3}
    for line in data:

        if line[1] == 'X':
            response = plays_as_ints[line[0]] - 1
            if response == 0:
                response = 3
            total_score += response

        elif line[1] == 'Y':
            total_score += 3 + plays_as_ints[line[0]]

        elif line[1] == 'Z':
            response = plays_as_ints[line[0]] + 1
            if response == 4:
                response = 1
            total_score += 6 + response

    print(total_score)


if __name__ == '__main__':
    with open('data/2.txt', 'rt') as data_file:
        round_data = [line.strip().split() for line in data_file]

    part_1(round_data)
    part_2(round_data)
