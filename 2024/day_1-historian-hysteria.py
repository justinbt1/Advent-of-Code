from collections import Counter


def part_one(list_a, list_b):
    list_a.sort()
    list_b.sort()

    diff_count = 0
    for a, b in zip(list_a, list_b):
        diff_count += abs(a - b)

    print(diff_count)


def part_two(list_a, list_b):
    count_b = Counter(list_b)
    similarity_score = 0
    for a in list_a:
        if count_b.get(a):
            similarity_score += a * count_b[a]

    print(similarity_score)            


if __name__ == '__main__':
    list_a = []
    list_b = []

    with open('2024/data/1.txt') as file:
        for row in file:
            a, b = row.split()
            list_a.append(int(a))
            list_b.append(int(b))

    part_one(list_a, list_b)
    part_two(list_a, list_b)
