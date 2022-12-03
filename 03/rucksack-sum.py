#!/usr/bin/env python3

import json
import logging


def main():
    score_lookup = get_score_lookup()
    logging.debug(score_lookup)
    lines = get_lines_from_file("personal-input.txt")

    sum = 0
    for line in lines:
        set_size = int(len(line)/2)
        set_1 = set(line[:set_size])
        set_2 = set(line[set_size:])
        intersect = set_1.intersection(set_2)
        assert(len(intersect) == 1)
        double_packed_item = intersect.pop()
        sum += score_lookup[double_packed_item]

    logging.info(f"Anser #1: {sum}")

    sum_2 = 0

    while lines:
        line_1 = lines.pop(0)
        line_2 = lines.pop(0)
        line_3 = lines.pop(0)

        intersect = set(line_1).intersection(set(line_2)).intersection(set(line_3))
        assert(len(intersect) == 1)
        group_item = intersect.pop()
        score = score_lookup[group_item]
        logging.debug(f"{group_item} - {score}")
        sum_2 += score

    print(sum_2)



def get_score_lookup() -> dict[str, int]:
    lower_chars = [chr(el) for el in range(ord('a'), ord('z') + 1)]
    upper_chars = [chr(el) for el in range(ord('A'), ord('Z') + 1)]
    return dict(zip(lower_chars + upper_chars, range(1, 53)))


def get_lines_from_file(input_file: str) -> list[str]:
    with open(input_file) as file:
        return file.read().splitlines()



if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    main()
