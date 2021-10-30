# Enter your code here. Read input from STDIN. Print output to STDOUT

import re

for _ in range(int(input())):
    print(bool(re.match(r'^[+-]?[0-9]*\.[0-9]+$', input())))
