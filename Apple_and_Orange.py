#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    apple_num = []
    oranges_num = []
    for apple in apples:
        if apple + a >= s and apple + a <= t:
            apple_num.append(apple)
    for orange in oranges:
        if orange + b <= t and orange + b >= s:
            oranges_num.append(orange)
    print(len(apple_num))
    print(len(oranges_num))


if __name__ == "__main__":
    # st = input().split()

    # s = int(st[0])

    # t = int(st[1])

    # ab = input().split()

    # a = int(ab[0])

    # b = int(ab[1])

    # mn = input().split()

    # m = int(mn[0])

    # n = int(mn[1])

    # apples = list(map(int, input().rstrip().split()))

    # oranges = list(map(int, input().rstrip().split()))

    s = 7
    t = 11
    a = 5
    b = 15
    apples = [-2, 2, 1]
    oranges = [5, -6]

    countApplesAndOranges(s, t, a, b, apples, oranges)
