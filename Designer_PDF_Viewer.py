#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the designerPdfViewer function below.
def designerPdfViewer(h, word):
    return len(word) * max([h[ord(w) - 97] for w in word])
    # word_len = len(word)
    # index = [(ord(w) - 97) for w in word]
    # index = max(index)
    # print(word_len * h[index])
    # return word_len * h[index]


if __name__ == "__main__":
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # h = list(map(int, input().rstrip().split()))

    # word = input()

    # result = designerPdfViewer(h, word)

    # fptr.write(str(result) + '\n')

    # fptr.close()

    h = [1, 3, 1, 3, 1, 4, 1, 3, 2, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 7]
    word = "zaba"

    # h = [1, 3, 1, 3, 1, 4, 1, 3, 2, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
    # word = "abc"

    designerPdfViewer(h, word)
