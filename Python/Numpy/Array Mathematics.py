import numpy

n, m = map(int, input().split())
a = numpy.array([input().strip().split() for _ in range(n)], int)
b = numpy.array([input().strip().split() for _ in range(n)], int)

print(numpy.add(a, b))
print(numpy.subtract(a, b))
print(numpy.multiply(a, b))
print(numpy.floor_divide(a, b))
print(numpy.mod(a, b))
print(numpy.power(a, b))
