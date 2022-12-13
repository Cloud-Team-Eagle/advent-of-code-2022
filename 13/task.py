#!/usr/bin/env python3



def main():
    lines = get_lines_from_file('demo-input.txt')

    while lines:
        left = lines.pop(0)
        right = lines.pop(0)



        if lines:
            empty = lines.pop(0)


def get_lines_from_file(input_file: str) -> list[str]:
    with open(input_file) as file:
        return file.read().splitlines()


if __name__ == "__main__":
    main()
