
class DirectoryNode:
    def __init__(self, name):
        self.name = name
        self.size = 0
        self.sub_nodes = {}
        self.parent = None


def tree_builder(cli_lines):
    current_node = None

    for line in cli_lines:
        line = line.strip().split()
        if line[0] == '$':
            if line[1] == 'cd':
                current_node = DirectoryNode(line[2])
        elif line[0] == 'dir':
            child_name = line[1]
            print(child_name)
            current_node.sub_nodes[child_name] = DirectoryNode(name=child_name)
        else:
            current_node.size += int(line[0])


if __name__ == '__main__':
    with open('data/7.txt', 'rt') as input_file:
        tree_builder(input_file)
