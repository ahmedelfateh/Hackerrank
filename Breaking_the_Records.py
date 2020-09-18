#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    hight_score = scores[0]
    low_score = scores[0]
    hight_scores = []
    low_scores = []
    for score in scores:
        if score > hight_score:
            hight_score = score
            hight_scores.append(hight_score)
        elif score < low_score:
            low_score = score
            low_scores.append(low_score)

    return len(hight_scores), len(low_scores)


if __name__ == "__main__":
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # n = int(input())

    # scores = list(map(int, input().rstrip().split()))

    # result = breakingRecords(scores)

    # fptr.write(' '.join(map(str, result)))
    # fptr.write('\n')

    # fptr.close()

    scores = [3, 4, 21, 36, 10, 28, 35, 5, 24, 42]

    breakingRecords(scores)
