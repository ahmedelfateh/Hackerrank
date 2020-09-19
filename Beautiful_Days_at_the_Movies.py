#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the beautifulDays function below.
def beautifulDays(i, j, k):
    count = 0
    for d in range(i, j + 1):
        rev_d = int(str(d)[::-1])
        if abs(i - rev_d) % k == 0:
            count += 1
    return count


if __name__ == "__main__":
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # ijk = input().split()

    # i = int(ijk[0])

    # j = int(ijk[1])

    # k = int(ijk[2])

    # result = beautifulDays(i, j, k)

    # fptr.write(str(result) + '\n')

    # fptr.close()

    i = 20
    j = 23
    k = 6
    result = beautifulDays(i, j, k)
