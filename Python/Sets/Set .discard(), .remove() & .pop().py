n = int(input())
s = set(map(int, input().split()))
for _ in range(int(input())):
    command = input().split()
    args = command[1:]
    command = command[0]
    command += "(" + ",".join(args) + ")"
    eval("s."+command)
print(sum(s))
