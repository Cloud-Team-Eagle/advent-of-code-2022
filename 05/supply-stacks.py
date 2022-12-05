#!/usr/bin/env python3


def main():
    stacks_data, moves_data = get_input_from_file("personal-input.txt")
    stacks = Stacks(stacks_data)

    for line in moves_data:
        word_list = line.split()
        quantity = int(word_list[1])
        src = int(word_list[3])
        dst = int(word_list[5])
        stacks.move_v2(quantity=quantity, src=src, dst=dst)

    print(stacks)
    print(stacks.result())


class Stacks:
    def __init__(self, lines) -> None:
        stack_count = int(lines.pop().split()[-1])
        self.stacks = [[] for i in range(0, stack_count)]
        while lines:
            line = lines.pop()
            for i in range(0, stack_count):
                if line[i*4] == "[":
                    self.stacks[i].append(line[i*4 + 1])

    def move_v1(self, quantity, src, dst) -> None:
        tmp = []
        for _ in range(0, quantity):
            tmp.append(self.stacks[src-1].pop())
        self.stacks[dst-1] += tmp

    def move_v2(self, quantity, src, dst) -> None:
        tmp = []
        for _ in range(0, quantity):
            tmp.append(self.stacks[src-1].pop())
        tmp.reverse()
        self.stacks[dst-1] += tmp

    def __str__(self) -> str:
        return str(self.stacks)
        
    def result(self) -> str:
        return "".join([s[-1] for s in self.stacks])


def get_input_from_file(input_file: str) -> list[list[str]]:
    with open(input_file) as file:
        data = file.read()
        parts = data.split("\n\n")
        return [part.split("\n") for part in parts]


if __name__ == "__main__":
    main()
