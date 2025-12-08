import numpy as np


def load_data():
    coordinates = []
    with open('2025/data/8.txt', 'rt') as buffer:
        for row in buffer:
            coordinates.append([int(n) for n in row.strip().split(',')])
        
    return np.array(coordinates)


def calculate_euclidians(data):
    tracker = []
    for i in range(data.shape[0] - 1):
        euclidean_distances = np.sqrt(np.sum((data[i + 1:] - data[i]) ** 2, axis=1))
        for j in range(data[i + 1:].shape[0]):
            tracker.append((euclidean_distances[j], (i, j + i + 1)))

    return  sorted(tracker)


def cluster_circuits(distances, n=1000):
    pairs = [set(distances[i][1]) for i in range(n)]
    for _ in range(len(pairs)):
        circuits = []
        merged = False
        a = pairs.pop(0)
        for b in pairs:
            if a & b:
                c = b | a
                circuits.append(c)
                merged = True
            else:
                circuits.append(b)

        if not merged:
            circuits.append(a)
            
        pairs = circuits

    print(np.prod(sorted([len(p) for p in pairs], reverse=True)[:3]))


if __name__ == '__main__':
    data = load_data()
    euclidiean_distances = calculate_euclidians(data)
    cluster_circuits(euclidiean_distances)
