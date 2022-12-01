#!/usr/bin/env python3

import json


def main():
    with open('personal-input.txt') as file:
        lines = file.read().splitlines()
        result = 0
        tmp = 0
        for line in lines:
            if line != "":
                tmp += int(line)
            else:
                if tmp > result:
                    result = tmp
                tmp = 0
        print(result)


def main2():
    with open('personal-input.txt') as file:
        lines = file.readlines()
        lines = [line.strip() for line in lines]
        lines = [int(line) if line != "" else None for line in lines]

        list_of_lists = []
        start = 0
        for i, line in enumerate(lines):
            if is_empty(line):
                list_of_lists.append(lines[start:i])
                start = i+1
        
        sums = [sum(list) for list in list_of_lists]
        sums = sorted(sums)

    print(json.dumps(list_of_lists, indent=4))
    print(json.dumps(sums, indent=4))
    print(max(sums))
    print(sum(sums[-3:]))


def is_empty(line):
    return not line



if __name__ == "__main__":
    main2()

