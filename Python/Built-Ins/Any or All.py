# Enter your code here. Read input from STDIN. Print output to STDOUT

N, arr = int(input()), input().split()
print(all([all([int(val) > 0 for val in arr]),
           any([val == val[::-1] for val in arr])]))
