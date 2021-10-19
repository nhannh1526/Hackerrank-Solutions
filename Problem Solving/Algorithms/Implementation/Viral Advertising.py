#!/bin/python3

import os


#
# Complete the 'viralAdvertising' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#


def viralAdvertising(n):
    # Write your code here
    shared = 5
    cumulative = 0
    for _ in range(n):
        liked = shared // 2
        cumulative += liked
        shared = liked * 3
    return cumulative


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()
