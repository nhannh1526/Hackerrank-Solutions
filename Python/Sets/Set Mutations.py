# Enter your code here. Read input from STDIN. Print output to STDOUT

a = int(input())
A = set(map(int, input().split()))

for _ in range(int(input())):
    cmd, b = input().split()
    B = set(map(int, input().split()))
    cmd += f"({B})"
    eval("A." + cmd)

print(sum(A))
