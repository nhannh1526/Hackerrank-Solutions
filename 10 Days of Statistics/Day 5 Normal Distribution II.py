# Enter your code here. Read input from STDIN. Print output to STDOUT

import math


def cdf(x, loc, scale):
    return 0.5 * (1 + math.erf((x - loc) / (scale * 2 ** 0.5)))


mu, sigma = map(int, input().split())
x1 = int(input())
x2 = int(input())

print(f"{100 * (1 - cdf(x1, mu, sigma)):.2f}",
      f"{100 * (1 - cdf(x2, mu, sigma)):.2f}",
      f"{100 * (cdf(x2, mu, sigma)):.2f}", sep="\n")
