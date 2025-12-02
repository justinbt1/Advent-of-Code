from time import time

def read_data():
    id_ranges = []
    with open('2025/data/2.txt', 'rt') as id_buffer:
        for id_range in id_buffer.read().split(','):
            id_tuple = tuple(int(i) for i in id_range.split('-'))
            id_ranges.append(id_tuple)

    return id_ranges


def mirrored_ids(seq):
    return seq[:len(seq)//2] == seq[len(seq)//2:]


def recurring_ids(seq):
    for n in range(2, len(seq) + 1):
        splits = [seq[i:i + len(seq) // n] for i in range(0, len(seq), len(seq) // n)]
        if len(set(splits)) == 1:
            return True


def check_sequences(id_ranges, detector):
    invalid_ids = 0
    for id_pair in id_ranges:
        for i in range(id_pair[0], id_pair[1] + 1):
            if detector(str(i)):
                invalid_ids += i

    print(invalid_ids)


if __name__ == '__main__':
    data = read_data()
    check_sequences(data, mirrored_ids)
    start = time()
    check_sequences(data, recurring_ids)
    print(time() - start)
