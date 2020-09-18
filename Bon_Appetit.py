#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the bonAppetit function below.
def bonAppetit(bill, k, b):
    total = sum(bill)
    bill.pop(k)
    total_k = sum(bill)
    if b == total / 2:
        refund = b - (total_k / 2)
        print(int(refund))
    else:
        print("Bon Appetit")


if __name__ == "__main__":
    # nk = input().rstrip().split()

    # n = int(nk[0])

    # k = int(nk[1])

    # bill = list(map(int, input().rstrip().split()))

    # b = int(input().strip())

    bill = [3, 10, 2, 9]
    k = 1
    b = 12

    bonAppetit(bill, k, b)
