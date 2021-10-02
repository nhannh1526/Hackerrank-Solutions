#!/bin/python3

if __name__ == '__main__':
    N = int(input().strip())
    if N % 2 == 1 or N in range(6, 21):
        print("Weird")
    else:
        print("Not Weird")
