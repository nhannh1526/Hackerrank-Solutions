# Enter your code here. Read input from STDIN. Print output to STDOUT
import math


def isPrime(n):
    if n == 2:
        return "Prime"
    if n == 1 or (n & 1) == 0:
        return "Not prime"
    for i in range(2, math.ceil(n ** 0.5) + 1):
        if n % i == 0:
            return "Not prime"
    return "Prime"


for _ in range(int(input())):
    print(isPrime(int(input())))
