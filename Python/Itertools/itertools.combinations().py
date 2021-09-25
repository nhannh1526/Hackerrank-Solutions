# Enter your code here. Read input from STDIN. Print output to STDOUT

from itertools import combinations

S, k = input().split()
for i in range(1, int(k)+1):
    print(*["".join(chars)
            for chars in list(combinations(sorted(S), i))], sep="\n")
