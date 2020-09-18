#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#


def getTotalX(a, b):
    # Write your code here
    f = []
    result = []
    m_len = len(a + b)
    for x in range(1, 101):
        for num in a:
            if x % num == 0:
                f.append(x)
    for x in range(1, 101):
        for num in b:
            if num % x == 0:
                f.append(x)
    for num in f:
        if f.count(num) == m_len:
            result.append(num)
    result = set(result)
    return len(result)


if __name__ == "__main__":
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # first_multiple_input = input().rstrip().split()

    # n = int(first_multiple_input[0])

    # m = int(first_multiple_input[1])

    # arr = list(map(int, input().rstrip().split()))

    # brr = list(map(int, input().rstrip().split()))

    # total = getTotalX(arr, brr)

    # fptr.write(str(total) + '\n')

    # fptr.close()

    arr = [2, 4]
    brr = [16, 32, 96]

    getTotalX(arr, brr)