#!/bin/python3

if __name__ == '__main__':

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    result = sum(arr[0][:3]) + arr[1][1] + sum(arr[2][:3])

    for i in range(1, len(arr) - 1):
        for j in range(1, len(arr) - 1):
            current_sum = sum(arr[i - 1][j - 1:j + 2]) + \
                          arr[i][j] + sum(arr[i + 1][j - 1:j + 2])
            if current_sum > result:
                result = current_sum
    print(result)
