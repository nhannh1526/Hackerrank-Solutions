# Enter your code here. Read input from STDIN. Print output to STDOUT

def factorial(x):
    if x == 0 or x == 1:
        return 1
    return x * factorial(x - 1)


def comb(n, k):
    return factorial(n) / (factorial(k) * factorial(n - k))


def binom(k, n, p):
    return comb(n, k) * p**k * (1 - p)**(n-k)


n = 6
boys, girls = map(float, input().split())
p = boys / (boys + girls)

print(f"{sum([binom(x, n, p) for x in range(3,7)]):.3f}")
