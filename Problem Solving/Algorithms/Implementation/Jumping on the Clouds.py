#!/bin/python3

import os


#
# Complete the 'jumpingOnClouds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY c as parameter.
#


def jumpingOnClouds(c):
    # Write your code here
    pos = 0
    result = 0
    while True:
        if pos + 2 < len(c) and c[pos + 2] != 1:
            pos += 2
        elif pos + 1 < len(c):
            pos += 1
        else:
            break
        result += 1
    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
