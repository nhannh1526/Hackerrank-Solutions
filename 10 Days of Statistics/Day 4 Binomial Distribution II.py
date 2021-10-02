# Enter your code here. Read input from STDIN. Print output to STDOUT

def factorial(x):
    if x == 0 or x == 1:
        return 1
    return x * factorial(x - 1)


def comb(n, k):
    return factorial(n) / (factorial(k) * factorial(n - k))


def binom(k, n, p):
    return comb(n, k) * p ** k * (1 - p) ** (n - k)


p, n = map(int, input().split())
print(f"{sum([binom(x, n, p * 0.01) for x in range(3)]):.3f}",
      f"{sum([binom(x, n, p * 0.01) for x in range(2, 11)]):.3f}", sep="\n")
