#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the viralAdvertising function below.
def viralAdvertising(n):
    init = 5
    result = 0
    for i in range(n):
        result += init // 2
        init = init // 2 * 3
    print(result)


if __name__ == "__main__":
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # n = int(input())

    # result = viralAdvertising(n)

    # fptr.write(str(result) + '\n')

    # fptr.close()

    n = 3

    viralAdvertising(n)
