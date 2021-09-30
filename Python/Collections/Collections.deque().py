# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import deque

d = deque()
for _ in range(int(input())):
    cmd, *args = input().split()
    getattr(d, cmd)(*args)

print(*d, sep=" ")
