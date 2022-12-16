
class DirectoryNode:
    def __init__(self, name, parent):
        self.name = name
        self.size = 0
        self.files = set()
        self.children = {}
        self.parent = parent

    def add_file(self, file, size):
        if file not in self.files:
            self.files.add(file)
            self.size += int(size)


def build_tree(cli_lines):
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
            current_node.add_file(line[1], line[0])

    while current_node.name != '/':
        current_node = current_node.parent

    return current_node


def walk_tree(tree, sizes):
    for child in tree.children:
        child_size, sizes = walk_tree(tree.children[child], sizes)
        tree.size += child_size
    sizes.append(tree.size)
    return tree.size, sizes


def part_one(file_size_list):
    small_directories = 0
    for file in file_size_list:
        if file > 100000:
            break

        small_directories += file

    print(f'Part 1: {small_directories}')


def part_two(file_size_list):
    space_needed = 30000000 - (70000000 - root_size)
    for file in size_list:
        if file >= space_needed:
            print(f'Part 2: {file}')
            break


if __name__ == '__main__':
    with open('data/7.txt', 'rt') as input_file:
        file_tree = build_tree(input_file)

    root_size, size_list = walk_tree(file_tree, [])
    size_list.sort()
    part_one(size_list)
    part_two(size_list)
