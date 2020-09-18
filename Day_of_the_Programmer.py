#!/bin/python3

import math
import os
import random
import re
import sys

# https://www.geeksforgeeks.org/program-check-given-year-leap-year/
# Complete the dayOfProgrammer function below.
def dayOfProgrammer(year):
    if year == 1918:
        result = "26.09.1918"
    elif ((year <= 1917) and (year % 4 == 0)) or (
        (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0))
    ):
        result = f"12.09.{format(year)}"
    else:
        result = f"13.09.{format(year)}"

    print(result)
    return result


if __name__ == "__main__":
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # year = int(input().strip())

    # result = dayOfProgrammer(year)

    # fptr.write(result + '\n')

    # fptr.close()

    year = 2016

    dayOfProgrammer(year)
