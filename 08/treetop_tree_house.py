#!/usr/bin/env python3

from enum import Enum
import json


def main():
    lines = get_lines_from_file('personal-input.txt')

    forest = [list(line) for line in lines]
    pretty_print(forest)
    
    max_x = len(forest[1])
    max_y = len(forest)

    visibility = [[False] * max_x for x in range(max_y)]
    scenic_score = [[0] * max_x for x in range(max_y)]

    for y in range(max_y):
        for x in range(max_x):
            if y == 0 or x == 0:
                visibility[y][x] = True
                
            elif y == max_y - 1 or x == max_x - 1:
                visibility[y][x] = True

            else:
                visibility[y][x] = is_visible(forest, x, y)
                scenic_score[y][x] = get_scenic_score(forest, x, y)


    # pretty_print(visibility)
    print(sum([sum([1 if x else 0 for x in xs]) for xs in visibility]))
    print(max([max(xs) for xs in scenic_score]))


def pretty_print(lines):
    print("---")
    for line in lines:
        print(line)
    print("---")
    

def is_visible(forest, x_point, y_point) -> bool:
    # check to north
    max_north = max([forest[y_pos][x_point] for y_pos in (list(range(y_point)))])
    if forest[y_point][x_point] > max_north:
        return True

    max_south = max([forest[y_pos][x_point] for y_pos in (list(range(y_point + 1, len(forest))))])
    if forest[y_point][x_point] > max_south:
        return True

    max_west = max([forest[y_point][x_pos] for x_pos in (list(range(x_point)))])
    if forest[y_point][x_point] > max_west:
        return True

    max_east = max([forest[y_point][x_pos] for x_pos in (list(range(x_point + 1, len(forest[0]))))])
    if forest[y_point][x_point] > max_east:
        return True

    return False


def get_scenic_score(forest, x_pos, y_pos) -> int:
    # look up north
    y_north_list = list(reversed(range(y_pos)))
    count_north = 1

    height = forest[y_pos][x_pos]
    stop = False
    for y_it in y_north_list:
        if stop:
            continue
        tree_height = forest[y_it][x_pos]
        if tree_height >= height:
            stop = True
        else:
            height = tree_height
            count_north += 1

    y_south_list = list(range(y_pos + 1, len(forest)))
    count_south = 0
    height = forest[y_pos][x_pos]
    stop = False
    for y_it in y_south_list:
        if stop:
            continue
        tree_height = forest[y_it][x_pos]
        if tree_height >= height:
            stop = True
            count_south += 1
        else:
            height = tree_height
            count_south += 1

    x_west_list = list(reversed(range(x_pos)))
    count_west = 0

    height = forest[y_pos][x_pos]
    stop = False
    for x_it in x_west_list:
        if stop:
            continue
        tree_height = forest[y_pos][x_it]
        if tree_height >= height:
            stop = True
            count_west += 1
        else:
            height = tree_height
            count_west += 1


    x_east_list = list(range(x_pos + 1, len(forest[0])))
    count_east = 0

    height = forest[y_pos][x_pos]
    stop = False
    for x_it in x_west_list:
        if stop:
            continue
        tree_height = forest[y_pos][x_it]
        if tree_height >= height:
            stop = True
            count_east += 1
        else:
            height = tree_height
            count_east += 1

    return count_north * count_south * count_east * count_west


def get_lines_from_file(input_file: str) -> list[str]:
    with open(input_file) as file:
        return file.read().splitlines()


if __name__ == "__main__":
    main()
