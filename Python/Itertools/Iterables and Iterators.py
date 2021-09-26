# Enter your code here. Read input from STDIN. Print output to STDOUT

from itertools import combinations

N = int(input())
letter_list = list(map(str, input().split()))
K = int(input())

c = list(combinations(letter_list, K))
print(sum([1 for t in c if "a" in t]) / len(c))
