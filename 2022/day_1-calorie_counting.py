
def get_top_3_elves():
    elf_calories_sum = 0
    totals = []
    with open('data/1A.txt', 'rt') as data_file:
        for row in data_file:
            if row.strip():
                elf_calories_sum += int(row)
            else:
                totals.append(elf_calories_sum)
                elf_calories_sum = 0

    totals.append(elf_calories_sum)
    totals.sort(reverse=True)

    return totals[:3]


if __name__ == '__main__':
    elves_highest_calorie = get_top_3_elves()
    print(f'Question 1 part A: {elves_highest_calorie[0]}')
    print(f'Question 1 part A: {sum(elves_highest_calorie)}')
