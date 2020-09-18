#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#


def countingValleys(steps, path):
    path_arr = []
    count = 0
    result = 0
    for s in path:
        path_arr.append(s)

    for i in range(steps):
        if path_arr[i] == "U":
            count += 1
            if count == 0:
                result += 1
        else:
            count -= 1

    print(result)


if __name__ == "__main__":
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # steps = int(input().strip())

    # path = input()

    # result = countingValleys(steps, path)

    # fptr.write(str(result) + '\n')

    # fptr.close()

    steps = 8
    path = "UDDDUDUU"
    # steps = 12
    # path = "DDUUDDUDUUUD"

    result = countingValleys(steps, path)