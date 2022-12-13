
class DirectoryNode:
    def __init__(self, name, parent):
        self.name = name
        self.size = 0
        self.children = {}
        self.parent = parent


def sum_directory(tree):
    for child in tree.children:
        tree.size += sum_directory(tree.children[child])

    print(tree.name, tree.size)

    return tree.size


def tree_builder(cli_lines):
    current_node = DirectoryNode(name='/', parent=None)

    for line in cli_lines:
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

    return current_node


if __name__ == '__main__':
    with open('data/7.txt', 'rt') as input_file:
        file_tree = tree_builder(input_file)

    while file_tree.name != '/':
        file_tree = file_tree.parent
    
    sum_directory(file_tree)
