# Enter your code here. Read input from STDIN. Print output to STDOUT

from itertools import product

A, B = list(map(int, input().split())), list(map(int, input().split()))
print(*list(product(A, B)), sep=" ")
