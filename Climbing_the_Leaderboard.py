#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'climbingLeaderboard' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY ranked
#  2. INTEGER_ARRAY player
#


def climbingLeaderboard(ranked, player):
    ranked = sorted(list(set(ranked)))
    index = 0
    result = []
    n = len(ranked)
    for p in player:
        while n > index and p >= ranked[index]:
            index += 1
        result.append(n + 1 - index)
    print(result)
    return result
    # result = []
    # for p in player:
    #     for r in ranked:
    #         if p >= r or p <= r:
    #             indx = ranked.index(r)
    #             ranked.pop(len(ranked) - 1)
    #             ranked.insert(indx, p)
    #             result.append(indx)
    # print(ranked)
    # print(result)

    # result = []
    # for p in player:
    #     for r in ranked:
    #         if p >= r:
    #             indx_r = ranked.index(r)
    #             indx_p = player.index(p)
    #             ranked.pop(len(ranked) - 1)
    #             ranked.insert(indx_r, p)
    #             player.pop(indx_p)
    #             result.append()
    # print(ranked)
    # print(result)


if __name__ == "__main__":
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # ranked_count = int(input().strip())

    # ranked = list(map(int, input().rstrip().split()))

    # player_count = int(input().strip())

    # player = list(map(int, input().rstrip().split()))

    # result = climbingLeaderboard(ranked, player)

    # fptr.write('\n'.join(map(str, result)))
    # fptr.write('\n')

    # fptr.close()

    ranked = [100, 100, 50, 40, 40, 20, 10]
    player = [5, 25, 50, 120]

    climbingLeaderboard(ranked, player)
