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
            try:
                if ''.join([matrix[m,n], matrix[m+1,n+1], matrix[m+2,n+2], matrix[m+3,n+3]]) in sub_string:
                    occurs += 1
            except IndexError:
                pass
            try:
                if n - 3 < 0:
                    continue
                elif ''.join([matrix[m,n], matrix[m+1,n-1], matrix[m+2,n-2], matrix[m+3,n-3]]) in sub_string:
                    occurs += 1
            except IndexError:
                pass

    print(occurs)


if __name__ == '__main__':
    search_matrix = []
    with open('2024/data/4.txt', 'rt') as file:
        for row in file:
            search_matrix.append((list(row.rstrip())))

    search_matrix = np.array(search_matrix)
    find_christmas(search_matrix, 'XMAS')
