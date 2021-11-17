import numpy

shape = tuple(map(int, input().split()))
print(numpy.zeros(shape, dtype=numpy.int64))
print(numpy.ones(shape, dtype=numpy.int64))
