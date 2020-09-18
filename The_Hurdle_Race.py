#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hurdleRace function below.
def hurdleRace(k, height):
    max_h = max(height)
    if k < max_h:
        result = max_h - k
    else:
        result = 0
    return result


if __name__ == "__main__":
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # nk = input().split()

    # n = int(nk[0])

    # k = int(nk[1])

    # height = list(map(int, input().rstrip().split()))

    # result = hurdleRace(k, height)

    # fptr.write(str(result) + '\n')

    # fptr.close()

    k = 4
    height = [1, 6, 3, 5, 2]

    hurdleRace(k, height)
