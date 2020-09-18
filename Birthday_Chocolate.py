#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the birthday function below.
def birthday(s, d, m):
    part = 0
    for i in range(len(s)):
        n = 0
        count = 0
        while n < (m):
            count += s[i + n]
            n += 1
        if count == d:
            part += 1
        if i + n == len(s):
            break
    print(part)
    return part


if __name__ == "__main__":
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # n = int(input().strip())

    # s = list(map(int, input().rstrip().split()))

    # dm = input().rstrip().split()

    # d = int(dm[0])

    # m = int(dm[1])

    # result = birthday(s, d, m)

    # fptr.write(str(result) + '\n')

    # fptr.close()

    s = [1, 2, 1, 3, 2]
    d = 3
    m = 2

    birthday(s, d, m)
