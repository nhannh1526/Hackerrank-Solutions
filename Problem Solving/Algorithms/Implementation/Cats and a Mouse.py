#!/bin/python3

import os


# Complete the catAndMouse function below.


def catAndMouse(x, y, z):
    x_z = abs(x - z)
    y_z = abs(y - z)
    return "Cat A" if x_z < y_z else "Cat B" if x_z > y_z else "Mouse C"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        xyz = input().split()

        x = int(xyz[0])

        y = int(xyz[1])

        z = int(xyz[2])

        result = catAndMouse(x, y, z)

        fptr.write(result + '\n')

    fptr.close()
