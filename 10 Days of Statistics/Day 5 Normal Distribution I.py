# Enter your code here. Read input from STDIN. Print output to STDOUT

import math


def cdf(x, loc, scale):
    return 0.5 * (1 + math.erf((x - loc) / (scale * 2**0.5)))


mu, sigma = map(int, input().split())
x = float(input())
x1, x2 = map(int, input().split())

print(f"{cdf(x, mu, sigma):.3f}",
      f"{cdf(x2, mu, sigma) - cdf(x1, mu, sigma):.3f}", sep="\n")
