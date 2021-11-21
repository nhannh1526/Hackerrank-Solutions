import numpy

a = numpy.array(list(map(int, input().split())), int)
b = numpy.array(list(map(int, input().split())), int)
print(numpy.inner(a, b))
print(numpy.outer(a, b))
