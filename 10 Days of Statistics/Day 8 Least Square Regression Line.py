# Enter your code here. Read input from STDIN. Print output to STDOUT

def fit(X, y):
    n = len(X)
    sum_X = sum(X)
    mu_X = sum_X / n
    sum_y = sum(y)
    mu_y = sum_y / n
    X_squared = sum([Xi ** 2 for Xi in X])
    Xy = sum([Xi * yi for Xi, yi in zip(X, y)])
    b = (n * Xy - sum_X * sum_y) / (n * X_squared - sum_X ** 2)
    a = mu_y - b * mu_X
    return a, b


def predict(X, a, b):
    return a + b * X


X, y = zip(*[map(int, input().split()) for _ in range(5)])
a, b = fit(X, y)
print(f"{predict(80, a, b):.3f}")
