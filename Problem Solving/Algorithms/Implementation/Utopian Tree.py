#!/bin/python3

import os


#
# Complete the 'utopianTree' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#


def utopianTree(n):
    # Write your code here
    if n < 3:
        return n + 1
    if n % 2:
        return utopianTree(n - 1) * 2
    return utopianTree(n - 1) + 1


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = utopianTree(n)

        fptr.write(str(result) + '\n')

    fptr.close()
