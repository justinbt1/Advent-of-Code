

def read_graph():
    adjacency_list = {}
    with open('2025/data/11.txt', 'rt') as input_buffer:
        for node_data in input_buffer:
            node_data = node_data.split()
            node = node_data[0][:-1]
            adjacency_list[node] = node_data[1:]
    
    adjacency_list['out'] = []
        
    return adjacency_list


def dfs(graph, start, target):
    stack = [(start, [start])]
    n_paths = 0
    
    while stack:
        node, path = stack.pop()

        if node == target:
            n_paths += 1
            continue

        for neighbor in reversed(graph.get(node, [])):
            if neighbor not in path:
                new_path = path + [neighbor]
                stack.append((neighbor, new_path))

    print(n_paths)


if __name__ == '__main__':
    graph = read_graph()
    dfs(graph, 'you', 'out')
