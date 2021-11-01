#!/bin/python3

import os


#
# Complete the 'appendAndDelete' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. STRING t
#  3. INTEGER k
#


def appendAndDelete(s, t, k):
    # Write your code here
    if k >= len(s) + len(t):
        return "Yes"

    prefix = 0
    for c1, c2 in zip(s, t):
        if c1 == c2:
            prefix += 1
        else:
            break

    if k >= len(s) + len(t) - 2 * prefix and k % 2 == (len(s) + len(t)) % 2:
        return "Yes"
    return "No"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    t = input()

    k = int(input().strip())

    result = appendAndDelete(s, t, k)

    fptr.write(result + '\n')

    fptr.close()
