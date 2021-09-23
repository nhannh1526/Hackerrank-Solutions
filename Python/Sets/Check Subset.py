# Enter your code here. Read input from STDIN. Print output to STDOUT

for _ in range(int(input())):
    a = int(input())
    A = set(map(int, input().split()))
    b = int(input())
    B = set(map(int, input().split()))
    if A.issubset(B):
        print(True)
    else:
        print(False)
