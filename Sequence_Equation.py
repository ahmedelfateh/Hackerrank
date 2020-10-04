#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the permutationEquation function below.
# https://www.youtube.com/watch?v=asSN2lKXcps&ab_channel=HackersRealm
def permutationEquation(p):
    result = []

    for i in range(1, len(p) + 1):
        result.append(p.index(p.index(i) + 1) + 1)
    print(result)


if __name__ == "__main__":
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # n = int(input())

    # p = list(map(int, input().rstrip().split()))

    # result = permutationEquation(p)

    # fptr.write('\n'.join(map(str, result)))
    # fptr.write('\n')

    # fptr.close()

    p = [4, 3, 5, 1, 2]

    permutationEquation(p)