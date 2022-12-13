
class DirectoryNode:
    def __init__(self, name, parent):
        self.name = name
        self.size = 0
        self.children = {}
        self.parent = parent


def tree_builder(cli_lines):
    current_node = DirectoryNode(name='/', parent=None)

    for line in cli_lines:
        print(current_node.name, current_node.size)
        line = line.strip().split()
        if line[0] == '$':
            if line[1] == 'cd':
                if line[2] == '..':
                    current_node = current_node.parent
                elif line[2] != '/':
                    current_node = current_node.children[line[2]]
        elif line[0] == 'dir':
            current_node.children[line[1]] = DirectoryNode(
                name=line[1],
                parent=current_node
            )
        else:
            current_node.size += int(line[0])


if __name__ == '__main__':
    with open('data/7.txt', 'rt') as input_file:
        tree_builder(input_file)
