#!/usr/bin/env python3


def main():
    lines = get_lines_from_file('personal-input.txt')

    cmds = []
    for line in lines:
        if line.startswith('noop'):
            cmds.append(0)

        elif line.startswith('addx'):
            arg = int(line.split()[1])
            # cmds.append(0)
            cmds.append(0)
            cmds.append(arg)

    cycle = 1
    x = 1
    sum = 0

    for cmd in cmds:

        if is_measurement_cycle(cycle):
            print(cycle, x, cycle * x)
            sum += cycle * x
        x += cmd

        cycle += 1

    print(sum)

def is_measurement_cycle(cycle):
    cycle -= 20
    while cycle >= 0:
        if cycle == 0:
            return True
        cycle -= 40
    return False
    

def get_lines_from_file(input_file: str) -> list[str]:
    with open(input_file) as file:
        return file.read().splitlines()


if __name__ == "__main__":
    main()
