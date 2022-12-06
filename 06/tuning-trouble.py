#!/usr/bin/env python3

import logging


def main():
    lines = get_lines_from_file('personal-input.txt')

    for line in lines:
        print(get_offset_end(line))


def get_offset_end(line: str) -> int:
    marker_length = 14
    for offset_end in range(marker_length-1, len(line)+1):
        # brute force because i'm lazy
        offset_start = offset_end - marker_length
        sequence_to_check = line[offset_start:offset_end]
        logging.debug(f"sequence_to_check: {sequence_to_check}")
        if len(set(sequence_to_check)) == marker_length:
            return offset_end


def get_lines_from_file(input_file: str) -> list[str]:
    with open(input_file) as file:
        return file.read().splitlines()



if __name__ == "__main__":
    main()
