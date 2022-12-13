#!/usr/bin/env python3



def main():
    lines = get_lines_from_file('demo-input.txt')


def get_lines_from_file(input_file: str) -> list[str]:
    with open(input_file) as file:
        return file.read().splitlines()


if __name__ == "__main__":
    main()
