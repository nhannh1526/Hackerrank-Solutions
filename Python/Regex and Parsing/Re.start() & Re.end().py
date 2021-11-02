# Enter your code here. Read input from STDIN. Print output to STDOUT

import re

S, k = input(), input()
m = re.search(k, S)
pattern = re.compile(k)

if not m:
    print("(-1, -1)")

while m:
    print(f"({m.start()}, {m.end() - 1})")
    m = pattern.search(S, m.start() + 1)
