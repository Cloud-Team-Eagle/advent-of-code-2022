#!/usr/bin/env python3

import logging

# this is very dirty!
my_sum = 0
additionally_required = 0
size_of_dir_to_delete = 0


def main():
    lines = get_lines_from_file('personal-input.txt')

    # optional: maybe the parent of root should also be root?
    root = Dir('/', None)  
    
    # doing the lazy version again :-/
    cwd = root
    for line in lines:
        if line.startswith('$ cd'):
            _, _, dir = line.split()
            logging.debug(f"cd {dir}")
            if dir == '..':
                cwd = cwd.parent
            elif dir == '/':
                cwd = root
            else:
                cwd = [x for x in cwd.children if x.name == dir][0]
        elif line.startswith('$ ls'):
            pass
        elif line.startswith('dir'):
            _, name = line.split()
            cwd.children.append(Dir(name, cwd))
        elif line.split()[0].isnumeric():
            size, name = line.split()
            cwd.children.append(File(name, int(size), cwd))

    print(root)
    print(my_sum)
    print(size_of_dir_to_delete)


class Node:
    def level(self) -> int:
        level = 0
        pos = self
        while pos.parent:
            level += 1
            pos = pos.parent
        return level

    def indent(self) -> str:
        return '  '*self.level()

    def __repr__(self) -> str:
        return self.name
        

class Dir(Node):
    def __init__(self, name, parent) -> None:
        self.name = name
        self.parent = parent
        self.children = []

    def __str__(self) -> str:
        # dirty, dirty, dirty!
        global my_sum, additionally_required, size_of_dir_to_delete

        result = f"{self.indent()}- {self.name} (dir)"

        current_size = self.size()
        result += f"  SUM: {current_size}"

        if current_size <= 100000:
            result += f"- SUM: {current_size}"
            my_sum += current_size

        if self.name == '/':
            print(f"occupied: {current_size}")
            print(f"free: {70000000 - current_size}")
            additionally_required = 30000000 - (70000000 - current_size)
            print(f"additionally required: {additionally_required}")
            size_of_dir_to_delete = current_size

        if additionally_required < current_size < size_of_dir_to_delete:
            size_of_dir_to_delete = current_size

        for child in self.children:
            result += f"\n{child}"
        return result

    def size(self) -> int:
        return sum([child.size() for child in self.children])


class File(Node):
    def __init__(self, name, size, parent) -> None:
        self.name = name
        self.file_size = size
        self.parent = parent

    def size(self) -> int:
        return self.file_size

    def __str__(self) -> str:
        return f"{self.indent()}- {self.name} (file, size:{self.file_size})"


def get_lines_from_file(input_file: str) -> list[str]:
    with open(input_file) as file:
        return file.read().splitlines()


if __name__ == "__main__":
    main()
