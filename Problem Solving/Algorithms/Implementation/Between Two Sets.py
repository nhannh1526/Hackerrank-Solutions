#!/bin/python3

import math
import os


def computeLCM(a, b):
    return a * b // math.gcd(a, b)


def getHCF(arr):
    hcf = arr[0]
    for i in arr:
        hcf = math.gcd(hcf, i)
    return hcf


def getLCM(arr):
    lcm = arr[0]
    for i in arr:
        lcm = computeLCM(lcm, i)
    return lcm


#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#


def getTotalX(a, b):
    # Write your code here
    lcm = getLCM(a)
    hcf = getHCF(b)
    return len([x for x in range(lcm, hcf + 1, lcm) if hcf % x == 0])


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()
