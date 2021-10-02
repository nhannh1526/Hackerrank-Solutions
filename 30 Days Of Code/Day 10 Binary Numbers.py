#!/bin/python3

if __name__ == '__main__':
    n = int(input().strip())
    print(len(max(bin(n).strip("0b").split("0"))))
