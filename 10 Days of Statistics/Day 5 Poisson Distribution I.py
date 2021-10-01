# Enter your code here. Read input from STDIN. Print output to STDOUT

import math


def poisson(k, mu):
    return math.exp(-mu) * mu**k / math.factorial(k)


mu, x = float(input()), int(input())

print(f"{poisson(x, mu):.3f}")
