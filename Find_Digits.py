#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the findDigits function below.
def findDigits(n):
    result = 0

    for i in list(str(n)):
        if int(i) != 0 and n % int(i) == 0:
            result += 1

    print(result)


if __name__ == "__main__":
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # t = int(input())

    # for t_itr in range(t):
    #     n = int(input())

    #     result = findDigits(n)

    #     fptr.write(str(result) + '\n')

    # fptr.close()

    n = 1012

    findDigits(n)
