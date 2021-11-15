import numpy


n, m = map(int, input().split())
arr = numpy.array([input().strip().split(' ') for _ in range(n)], int)
print(arr.transpose())
print(arr.flatten())
