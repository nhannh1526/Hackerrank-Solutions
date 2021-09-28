#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'stdDev' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#


def stdDev(arr):
    # Print your answers to 1 decimal place within this function
    mean = sum(arr) / len(arr)
    print(f"{(sum([(val-mean)**2 for val in arr])/len(arr))**0.5:.1f}")


if __name__ == '__main__':
    n = int(input().strip())

    vals = list(map(int, input().rstrip().split()))

    stdDev(vals)
