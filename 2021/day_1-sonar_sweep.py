def count_increase(depths, window=1):
    increases = 0
    for i in range(1, len(depths)):
        if sum(depths[i:i+window]) > sum(depths[i - 1: i + window - 1]):
            increases += 1

    print(increases)


if __name__ == '__main__':
    with open('2021/data/1.txt', 'rt') as file:
        depth_list = [int(line.strip()) for line in file]

    count_increase(depth_list)
    count_increase(depth_list, 3)
