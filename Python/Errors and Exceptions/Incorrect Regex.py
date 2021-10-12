# Enter your code here. Read input from STDIN. Print output to STDOUT

import re


def isvalidregex(regex):
    try:
        re.compile(regex)
    except re.error:
        return False
    return True


for _ in range(int(input())):
    print(isvalidregex(input()))
