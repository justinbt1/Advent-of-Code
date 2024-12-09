def create_array(disk_map):
    disk_array = []
    n = 0
    for i in range(0, len(disk_map), 2):
        disk_array.extend([str(n)] * int(disk_map[i]))
        n += 1
        try:
            disk_array.extend(['.'] * (int(disk_map[i + 1])))
        except IndexError:
            break

    return disk_array


def move_fragment(disk_array, fragment):
    for i in range(0, len(disk_array)):
        if disk_array[i] == '.':
            disk_array[i] = fragment
            return disk_array


def defrag(disk_array):
    while True:
        fragment = disk_array.pop()
        if fragment != '.':
            new_array = move_fragment(disk_array, fragment)
            if new_array:
                disk_array = new_array
            else:
                disk_array.append(fragment)
                break

    return disk_array


def calculate_filesystem_checksum(compact_array):
    checksum = 0
    for i, n in enumerate(compact_array):
        checksum += i * int(n)

    print(checksum)


if __name__ == '__main__':
    with open('2024/data/9.txt', 'rt') as file:
        disk_map = list(file.read().strip())

    array = create_array(disk_map)
    defragged_array = defrag(array)
    calculate_filesystem_checksum(defragged_array)
