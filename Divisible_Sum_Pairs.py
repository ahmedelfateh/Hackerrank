#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the divisibleSumPairs function below.
def divisibleSumPairs(n, k, ar):
    result = []
    ar.sort()
    for i in range(len(ar)):
        for x in range(i + 1, len(ar)):
            if (ar[i] + ar[x]) % k == 0:
                result.append(1)
    return len(result)


if __name__ == "__main__":
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # nk = input().split()

    # n = int(nk[0])

    # k = int(nk[1])

    # ar = list(map(int, input().rstrip().split()))

    # result = divisibleSumPairs(n, k, ar)

    # fptr.write(str(result) + '\n')

    # fptr.close()

    k = 3
    n = 6
    ar = [1, 3, 2, 6, 1, 2]

    divisibleSumPairs(n, k, ar)
