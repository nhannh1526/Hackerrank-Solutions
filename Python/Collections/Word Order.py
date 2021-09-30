# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import OrderedDict

ordinary_dictionary = OrderedDict()
for _ in range(int(input())):
    words = str(input())
    ordinary_dictionary[words] = ordinary_dictionary.get(
        words, 0) + 1

print(len(ordinary_dictionary.keys()))
print(*ordinary_dictionary.values(), sep=" ")
