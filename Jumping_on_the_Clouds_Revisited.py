#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c, k):

    e = 100
    i = 0

    while True:
        e = e - 1 - 2 * c[i]
        i = (i + k) % n
        # https://en.wikipedia.org/wiki/Modulo_operation
        if i == 0:
            break

    return e


if __name__ == "__main__":
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # nk = input().split()

    # n = int(nk[0])

    # k = int(nk[1])

    # c = list(map(int, input().rstrip().split()))

    # result = jumpingOnClouds(c, k)

    # fptr.write(str(result) + '\n')

    # fptr.close()

    c = [0, 0, 1, 0, 0, 1, 1, 0]
    k = 2

    jumpingOnClouds(c, k)
