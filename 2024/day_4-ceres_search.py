def find_christmas(matrix):
    for x in range(len(matrix[0])):
        for y in range(len(matrix)):
            if matrix[y][x] == 'X':
                print(matrix[y][x])
            else:
                print('#')


if __name__ == '__main__':
    search_matrix = []
    with open('2024/data/4.txt', 'rt') as file:
        for row in file:
            search_matrix.append(list(row.rstrip()))

    find_christmas(search_matrix)
