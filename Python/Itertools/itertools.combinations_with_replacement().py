# Enter your code here. Read input from STDIN. Print output to STDOUT

from itertools import combinations_with_replacement

S, k = input().split()
print(*["".join(chars)
        for chars in list(combinations_with_replacement(sorted(S), int(k)))], sep="\n")
