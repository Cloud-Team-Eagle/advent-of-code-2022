#!/usr/bin/env python3

import json

# A, X -> Rock
# B, Y -> Paper
# C, Z -> Sissors
#
# 1 for Rock, 
# 2 for Paper, and 
# 3 for Scissors
#
# 0 if you lost, 
# 3 if the round was a draw, and 
# 6 if you won
#
# X means you need to lose, 
# Y means you need to end the round in a draw, and 
# Z means you need to win"

def main():
    list = get_input_from_file("personal-input.txt")

    symbol_score = { 
        'X': 1,
        'Y': 2,
        'Z': 3
    }
    second_score = {
        'A': {
            'X': 0 + 3, 
            'Y': 3 + 1,
            'Z': 6 + 2
        },
        'B': {
            'X': 0 + 1, 
            'Y': 3 + 2,
            'Z': 6 + 3 
        },
        'C': {
            'X': 0 + 2, 
            'Y': 3 + 3,
            'Z': 6 + 1
        }
    }

    win_score = {
        'A': {
            'X': 3, 
            'Y': 6,
            'Z': 0
        },
        'B': {
            'X': 0, 
            'Y': 3,
            'Z': 6
        },
        'C': {
            'X': 6, 
            'Y': 0,
            'Z': 3
        }
    }

    sum = 0
    sum2 = 0

    for game in list:
        input_1 = game[0]
        input_2 = game[2]
        score_1 = symbol_score[input_2]
        score_2 = win_score[input_1][input_2]
        score_sum = score_1 + score_2

        # print(input_1, input_2)
        # print(score_1, score_2, score_sum)
        # print()
        sum += score_sum
        sum2 += second_score[input_1][input_2]

    print(sum)
    print(sum2)

    # print(json.dumps(list, indent=4))


def get_input_from_file(input_file):
    with open(input_file) as file:
        return file.read().splitlines()



if __name__ == "__main__":
    main()

