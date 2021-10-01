# Enter your code here. Read input from STDIN. Print output to STDOUT

for _ in range(int(input())):
    n = int(input())
    blocks = list(map(int, input().split()))
    idx = 0

    while idx < n - 1 and blocks[idx] >= blocks[idx+1]:
        idx += 1
    while idx < n - 1 and blocks[idx] <= blocks[idx+1]:
        idx += 1

    print("Yes" if idx == n-1 else "No")
