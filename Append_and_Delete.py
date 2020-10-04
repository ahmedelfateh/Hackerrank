#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the appendAndDelete function below.
def appendAndDelete(s, t, k):
    min_len = min(len(s), len(t))
    new_index = min_len

    for i in range(min_len):
        if s[i] != t[i]:
            new_index = i
            break

    ops = len(s) + len(t) - 2 * new_index

    if k == ops or (k >= ops and (k - ops) % 2 == 0) or k >= len(s) + len(t):
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # s = input()

    # t = input()

    # k = int(input())

    # result = appendAndDelete(s, t, k)

    # fptr.write(result + '\n')

    # fptr.close()

    s = "hackerhappy"
    t = "hackerrank"
    k = 9

    appendAndDelete(s, t, k)