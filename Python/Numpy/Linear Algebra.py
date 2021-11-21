import numpy

numpy.set_printoptions(legacy='1.13')

n = int(input())
print(numpy.linalg.det(numpy.array(
    [input().strip().split() for _ in range(n)], float)))
