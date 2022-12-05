#!/usr/bin/env python3

import logging
from dataclasses import dataclass


def main():
    lines = get_lines_from_file("personal-input.txt")

    include_sum = 0
    overlap_sum = 0

    for line in lines:
        task_a, task_b = get_tasks_from_line(line)
        if task_a.includes(task_b) or task_b.includes(task_a):
            include_sum += 1
        if task_a.overlaps(task_b):
            overlap_sum += 1
    
    print(include_sum)
    print(overlap_sum)


def get_tasks_from_line(line):
    a, b = [CleanupTask(it) for it in line.split(',')]
    logging.debug(f"a: {a}")
    logging.debug(f"b: {b}")
    logging.debug(f"a includes b: {a.includes(b)}")
    logging.debug(f"b includes a: {b.includes(a)}")
    logging.debug(f"total: {a.includes(b) or b.includes(a)}")
    logging.debug("---")
    logging.debug(f"a overlaps b: {a.overlaps(b)}")
    logging.debug("===")
    return [a, b]


@dataclass
class CleanupTask:
    start: int
    end: int

    def __init__(self, input):
        self.start, self.end = map(int, input.split('-'))

    def includes(self, other):
        return self.start <= other.start and self.end >= other.end
    
    def overlaps(self, other):
        a = set(range(self.start, self.end+1))
        b = set(range(other.start, other.end+1))
        overlap = a.intersection(b)
        return bool(overlap)


def get_lines_from_file(input_file: str) -> list[str]:
    with open(input_file) as file:
        return file.read().splitlines()



if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    main()
