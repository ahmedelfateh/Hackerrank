#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    count = 0
    result = []
    for i in range(n):
        if ar[i] not in result:
            result.append(ar[i])
        else:
            # result.pop(ar[i])❌
            result.remove(ar[i])
            count += 1

    return count


if __name__ == "__main__":
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # n = int(input())

    # ar = list(map(int, input().rstrip().split()))

    # result = sockMerchant(n, ar)

    # fptr.write(str(result) + '\n')

    # fptr.close()

    ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]
    n = 9

    sockMerchant(n, ar)

    # count_t = 0
    # print(round((count_t / 2))) #this to return the singel ones
    # ar = [10, 20, 20, 10, 10, 30, 50, 10, 20, 50, 100]
    # n = 11