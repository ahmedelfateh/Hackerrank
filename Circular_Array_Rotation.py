#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the circularArrayRotation function below.
def circularArrayRotation(a, k, queries):
    len_a = len(a)
    n_a = []
    for x in range(k):
        num = a[len_a - 1]
        a.insert(0, num)
        a.pop(len_a)

    for m in queries:
        n_a.append(a[m])

    return n_a


if __name__ == "__main__":
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # nkq = input().split()

    # n = int(nkq[0])

    # k = int(nkq[1])

    # q = int(nkq[2])

    # a = list(map(int, input().rstrip().split()))

    # queries = []

    # for _ in range(q):
    #     queries_item = int(input())
    #     queries.append(queries_item)

    # result = circularArrayRotation(a, k, queries)

    # fptr.write('\n'.join(map(str, result)))
    # fptr.write('\n')

    # fptr.close()

    a = [1, 2, 3]
    k = 2
    queries = [0, 1, 2]

    circularArrayRotation(a, k, queries)
