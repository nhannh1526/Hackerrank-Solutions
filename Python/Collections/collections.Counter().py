# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import Counter

X = int(input())
shoe_sizes = Counter(map(int, input().split()))
total_revenue = 0

for _ in range(int(input())):
    shoe_size, price = map(int, input().split())
    if shoe_sizes[shoe_size] > 0:
        shoe_sizes[shoe_size] -= 1
        total_revenue += price
print(total_revenue)
