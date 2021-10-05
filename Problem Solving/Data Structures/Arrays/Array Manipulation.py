#!/bin/python3

import os


#
# Complete the 'arrayManipulation' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#


def arrayManipulation(n, queries):
    # Write your code here
    arr = [0] * n
    for q in queries:
        start, end = q[0] - 1, q[1]
        arr[start] += q[2]
        if end != n:
            arr[end] -= q[2]

    itt, maxval = 0, 0
    for val in arr:
        itt += val
        if itt > maxval:
            maxval = itt
    return maxval


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
