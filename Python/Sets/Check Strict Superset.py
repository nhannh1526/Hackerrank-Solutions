# Enter your code here. Read input from STDIN. Print output to STDOUT

A = set(map(int, input().split()))
print(all([A.issuperset(set(map(int, input().split())))
           for i in range(int(input()))]))
