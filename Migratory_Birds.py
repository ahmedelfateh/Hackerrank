#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the migratoryBirds function below.
def migratoryBirds(arr):
    # arr_set = set(arr)
    # arr_copy = list(arr_set)
    # results = []
    # for item in arr_copy:
    #     results.append(arr.count(item))
    freq_arr = [0] * 6
    for x in range(len(arr)):
        freq_arr[arr[x]] += 1
    return freq_arr.index(max(freq_arr))


if __name__ == "__main__":
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # arr_count = int(input().strip())

    # arr = list(map(int, input().rstrip().split()))

    # result = migratoryBirds(arr)

    # fptr.write(str(result) + '\n')

    # fptr.close()

    arr = [1, 2, 3, 4, 5, 4, 3, 2, 1, 3, 4]
    # arr = [1, 4, 4, 4, 5, 3]
    migratoryBirds(arr)
