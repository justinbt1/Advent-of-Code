import numpy as np


def find_christmas(matrix, sub_string):
    occurs = 0
    sub_string = [sub_string, sub_string[::-1]]
    for m in range(len(matrix)):
        for n in range(len(matrix[0])):
            if ''.join(matrix[m, n:n + 4]) in sub_string:
                occurs += 1
            if ''.join(matrix[m:m + 4, n]) in sub_string:
                occurs += 1
            if m + 3 >= len(matrix):
                continue
            if n + 3 < len(matrix[0]):
                if ''.join([matrix[m+i, n+i] for i in [*range(0, 4)]]) in sub_string:
                    occurs += 1
            if n - 3 >= 0:
                if ''.join([matrix[m+i, n-i] for i in [*range(0, 4)]]) in sub_string:
                    occurs += 1

    print(occurs)


def find_x_mas(matrix):
    occurs = 0
    sub_string = ['MASMS', 'SAMMS', 'MASSM', 'SAMSM']
    for m in range(len(matrix) - 2):
        for n in range(len(matrix[0]) - 2):
            chars = [
                matrix[m,n],
                matrix[m+1,n+1],
                matrix[m+2,n+2],
                matrix[m+2,n],
                matrix[m,n+2]
            ]

            if ''.join(chars) in sub_string:
                occurs += 1

    print(occurs)


if __name__ == '__main__':
    search_matrix = []
    with open('2024/data/4.txt', 'rt') as file:
        for row in file:
            search_matrix.append((list(row.rstrip())))

    search_matrix = np.array(search_matrix)
    find_christmas(search_matrix, 'XMAS')
    find_x_mas(search_matrix)
