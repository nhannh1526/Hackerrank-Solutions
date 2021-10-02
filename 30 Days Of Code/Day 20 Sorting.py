#!/bin/python3

if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    # Write your code here
    numberOfSwaps = 0
    for i in range(n):
        currentSwaps = 0
        for j in range(n - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                currentSwaps += 1
        if currentSwaps == 0:
            break
        numberOfSwaps += currentSwaps

    print(
        f"Array is sorted in {numberOfSwaps} swaps.\nFirst Element: {a[0]}\nLast Element: {a[-1]}")
