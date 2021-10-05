#!/bin/python3


#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#


def plusMinus(arr):
    # Write your code here
    print(f"{sum([val > 0 for val in arr]) / len(arr):.6f}",
          f"{sum([val < 0 for val in arr]) / len(arr):.6f}",
          f"{sum([val == 0 for val in arr]) / len(arr):.6f}", sep="\n")


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
