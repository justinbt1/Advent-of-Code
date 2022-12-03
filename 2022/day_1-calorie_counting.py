
def question_1_part_a():
    max_calories = 0
    elf_calories_sum = 0

    with open('../data/1A.txt', 'rt') as data_file:
        for row in data_file:
            if row:
                print(row)

if __name__ == '__main__':
    question_1_part_a()