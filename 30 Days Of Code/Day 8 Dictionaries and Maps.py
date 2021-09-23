# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

phoneBook = {}
for _ in range(int(input())):
    contact = input().split()
    phoneBook[contact[0]] = contact[1]

for line in sys.stdin.readlines():
    name = line.strip()
    if name in phoneBook:
        print(f"{name}={phoneBook[name]}")
    else:
        print("Not found")
