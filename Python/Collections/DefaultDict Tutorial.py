# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import defaultdict

d = defaultdict(list)
n, m = map(int, input().split())

for i in range(1, n + 1):
    d[str(input())].append(i)

for _ in range(m):
    word = str(input())
    if word in d:
        print(*d[word], sep=" ")
    else:
        print(-1)
