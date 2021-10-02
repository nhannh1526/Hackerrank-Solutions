# Enter your code here. Read input from STDIN. Print output to STDOUT

import math


def cdf(x, loc, scale):
    return 0.5 * (1 + math.erf((x - loc) / (scale * 2 ** 0.5)))


x, n = int(input()), int(input())
mu, sigma = float(input()), float(input())

mu = mu * n
sigma = sigma * n ** 0.5

print(f"{cdf(x, mu, sigma):.4f}")
