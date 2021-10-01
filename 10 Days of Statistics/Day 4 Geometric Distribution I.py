# Enter your code here. Read input from STDIN. Print output to STDOUT

def geom(k, p):
    return (1 - p)**(k - 1) * p


numerator, denominator = map(int, input().split())
p = numerator / denominator
x = int(input())

print(f"{geom(x, p):.3f}")
