# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import OrderedDict

ordinary_dictionary = OrderedDict()
for _ in range(int(input())):
    item_name, space, price = input().rpartition(' ')
    ordinary_dictionary[item_name] = ordinary_dictionary.get(
        item_name, 0) + int(price)

for item_name, price in ordinary_dictionary.items():
    print(item_name, price)
