# Enter your code here. Read input from STDIN. Print output to STDOUT

def mean(a):
    return sum(a) / len(a)


def std(a):
    mu = mean(a)
    return (sum([(val - mu) ** 2 for val in a]) / len(a)) ** 0.5


def cov(m, y):
    mu_m = mean(m)
    mu_y = mean(y)
    return sum([(mi - mu_m) * (yi - mu_y) for mi, yi in zip(m, y)]) / len(m)


def pearsonr(x, y):
    return cov(x, y) / (std(x) * std(y))


n = int(input())
X = list(map(float, input().split()))
Y = list(map(float, input().split()))
print(f"{pearsonr(X, Y):.3f}")
