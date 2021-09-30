# Enter your code here. Read input from STDIN. Print output to STDOUT

def geom(k, p):
    return (1 - p) ** (k - 1) * p


numerator, denominator = map(int, input().split())
p = numerator / denominator
n = int(input())

print(f"{sum([geom(x, p) for x in range(1, n+1)]):.3f}")
