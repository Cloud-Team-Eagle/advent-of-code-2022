#!/usr/bin/env python3

import logging
from dataclasses import dataclass


def main():
    lines = get_lines_from_file("personal-input.txt")

    sum = 0
    for line in lines:
        task_a, task_b = get_tasks_from_line(line)
        if task_a.includes(task_b) or task_b.includes(task_a):
            sum += 1
    print(sum)


def get_tasks_from_line(line):
    a, b = [CleanupTask(it) for it in line.split(',')]
    logging.info(f"a: {a}")
    logging.info(f"b: {b}")
    logging.info(f"includes: {a.includes(b)}")
    logging.info(f"includes: {b.includes(a)}")
    logging.info(f"total: {a.includes(b) or b.includes(a)}")
    logging.info("---")
    return [a, b]


@dataclass
class CleanupTask:
    start: int
    end: int

    def __init__(self, input):
        self.start, self.end = map(int, input.split('-'))

    def includes(self, other):
        return self.start <= other.start and self.end >= other.end
    

def get_lines_from_file(input_file: str) -> list[str]:
    with open(input_file) as file:
        return file.read().splitlines()



if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    main()
