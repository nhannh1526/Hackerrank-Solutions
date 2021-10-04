#!/bin/python3

import os


#
# Complete the 'hourglassSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#


def hourglassSum(arr):
    # Write your code here
    result = sum(arr[0][:3]) + arr[1][1] + sum(arr[2][:3])
    for i in range(1, len(arr) - 1):
        for j in range(1, len(arr) - 1):
            current_sum = sum(arr[i - 1][j - 1:j + 2]) + \
                          arr[i][j] + sum(arr[i + 1][j - 1:j + 2])
            if current_sum > result:
                result = current_sum
    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
