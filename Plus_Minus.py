#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    nega = []
    posa = []
    zero = []
    for num in arr:
        if num > 0:
            posa.append(num)
        elif num < 0:
            nega.append(num)
        else:
            zero.append(num)

    try:
        posa_re = len(posa) / len(arr)
        # print(round(posa_re, 6))
        print(f"{posa_re:9.6f}")
    except:
        pass

    try:
        nega_re = len(nega) / len(arr)
        # print(round(nega_re, 6))
        print(f"{nega_re:9.6f}")
    except:
        pass

    try:
        zero_re = len(zero) / len(arr)
        # print(round(zero_re, 6))
        print(f"{zero_re:9.6f}")
    except:
        pass


if __name__ == "__main__":
    n = int(input())

    # arr = list(map(int, input().rstrip().split()))
    arr = [-4, 3, -9, 0, 4, 1]

    plusMinus(arr)
