#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'interQuartile' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY values
#  2. INTEGER_ARRAY freqs
#


def median(arr):
    length_arr = len(arr)
    if length_arr % 2 == 0:
        return int(sum(sorted(arr)[int(length_arr/2-1):int(length_arr/2+1)])/2)
    return sorted(arr)[int((length_arr + 1)/2-1)]


def interQuartile(values, freqs):
    # Print your answer to 1 decimal place within this function
    arr = []
    for i in range(len(values)):
        arr += [values[i]] * freqs[i]
    arr.sort()
    length_arr = len(arr)
    Q1 = median(arr[:int(length_arr/2)])
    if length_arr % 2 == 0:
        Q3 = median(arr[int(length_arr/2):])
    else:
        Q3 = median(arr[int(length_arr/2+1):])
    print(f"{Q3-Q1:.1f}")


if __name__ == '__main__':
    n = int(input().strip())

    val = list(map(int, input().rstrip().split()))

    freq = list(map(int, input().rstrip().split()))

    interQuartile(val, freq)
