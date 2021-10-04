#!/bin/python3

import os


#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#


def diagonalDifference(arr):
    # Write your code here
    n = len(arr)
    primary_diagonal = [arr[i][i] for i in range(n)]
    secondary_diagonal = [arr[i][n - 1 - i] for i in range(n)]
    return abs(sum(primary_diagonal) - sum(secondary_diagonal))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
