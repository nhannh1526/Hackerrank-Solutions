#!/bin/python3

import os


#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#


def breakingRecords(scores):
    # Write your code here
    Minimum, Maximum = scores[0], scores[0]
    Min, Max = 0, 0
    for score in scores:
        if score < Minimum:
            Minimum = score
            Min += 1
        if score > Maximum:
            Maximum = score
            Max += 1
    return Max, Min


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
