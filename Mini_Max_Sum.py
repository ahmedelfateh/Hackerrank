#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    arr.sort()
    arr_len = len(arr)
    x_min = arr.copy()
    x_min.pop(arr_len - 1)
    min_x = sum(x_min)
    x_max = arr.copy()
    x_max.pop(0)
    max_x = sum(x_max)

    print(f"{min_x} {max_x}")


if __name__ == "__main__":
    # arr = list(map(int, input().rstrip().split()))

    arr = [1, 2, 3, 4, 5]

    miniMaxSum(arr)
