# Enter your code here. Read input from STDIN. Print output to STDOUT

import numpy as np


def fit(X, y):
    return np.dot(np.dot(np.linalg.inv(np.dot(X.T, X)), X.T), y)


def predict(X, matrixB):
    return np.dot(X, matrixB)


m, n = map(int, input().split())
X, y = [], []
for _ in range(n):
    line = list(map(float, input().split()))
    X.append([1] + line[:-1])
    y.append(line[-1])

X = np.array(X, dtype=float)
y = np.array(y, dtype=float)
matrixB = fit(X, y)

q = int(input())
for _ in range(q):
    print(
        f"{predict(np.array([1] + list(map(float, input().split())), dtype=float), matrixB):.2f}")
