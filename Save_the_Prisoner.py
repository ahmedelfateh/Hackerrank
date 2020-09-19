#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the saveThePrisoner function below.
# https://www.youtube.com/watch?v=NFL3K8cU56Q&ab_channel=HackersRealm 👏🏼👏🏼👏🏼👏🏼👏🏼
# https://codereview.stackexchange.com/questions/135677/save-the-prisoner
def saveThePrisoner(n, m, s):
    result = s + m - 1
    result %= n
    if result == 0:
        return n
    else:
        return result


if __name__ == "__main__":
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # t = int(input())

    # for t_itr in range(t):
    #     nms = input().split()

    #     n = int(nms[0])

    #     m = int(nms[1])

    #     s = int(nms[2])

    #     result = saveThePrisoner(n, m, s)

    #     fptr.write(str(result) + '\n')

    # fptr.close()

    n = 5
    m = 2
    s = 1

    result = saveThePrisoner(n, m, s)
