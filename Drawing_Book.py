#!/bin/python3

import os
import sys
import math

#
# Complete the pageCount function below.
#
def pageCount(n, p):
    # if p <= n and p / 2 > (n / 2 - p / 2):
    #     result = n / 2 - p / 2
    #     print((result))
    # else:
    #     result = p / 2
    #     print((result))
    # Floor division
    if p <= n and p // 2 > (n // 2 - p // 2):
        result = n // 2 - p // 2
        print((result))
    else:
        result = p // 2
        print((result))


if __name__ == "__main__":
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # n = int(input())

    # p = int(input())

    # result = pageCount(n, p)

    # fptr.write(str(result) + '\n')

    # fptr.close()

    n = 5
    p = 4

    pageCount(n, p)