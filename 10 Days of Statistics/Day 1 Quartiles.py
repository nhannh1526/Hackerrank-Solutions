#!/bin/python3

import os


#
# Complete the 'quartiles' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#


def median(arr):
    length_arr = len(arr)
    if length_arr % 2 == 0:
        return int(sum(sorted(arr)[int(length_arr / 2 - 1):int(length_arr / 2 + 1)]) / 2)
    return sorted(arr)[int((length_arr + 1) / 2 - 1)]


def quartiles(arr):
    # Write your code here
    tmp_arr = sorted(arr)
    length_arr = len(tmp_arr)
    Q1 = median(tmp_arr[:int(length_arr / 2)])
    Q2 = median(tmp_arr)
    if length_arr % 2 == 0:
        Q3 = median(tmp_arr[int(length_arr / 2):])
    else:
        Q3 = median(tmp_arr[int(length_arr / 2 + 1):])
    return Q1, Q2, Q3


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    data = list(map(int, input().rstrip().split()))

    res = quartiles(data)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
