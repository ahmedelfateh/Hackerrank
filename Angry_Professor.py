#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the angryProfessor function below.
def angryProfessor(k, a):
    arrived_stu = []
    for t in a:
        if t <= 0:
            arrived_stu.append(t)

    num = len(arrived_stu)
    if num >= k:
        return "NO"
    else:
        return "YES"


if __name__ == "__main__":
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # t = int(input())

    # for t_itr in range(t):
    #     nk = input().split()

    #     n = int(nk[0])

    #     k = int(nk[1])

    #     a = list(map(int, input().rstrip().split()))

    #     result = angryProfessor(k, a)

    #     fptr.write(result + '\n')

    # fptr.close()

    k = 3
    a = [-1, -3, 4, 2]
    # k = 2
    # a = [0, -1, 2, 1]

    angryProfessor(k, a)
