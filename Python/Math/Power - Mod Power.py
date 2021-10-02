# Enter your code here. Read input from STDIN. Print output to STDOUT

a, b, m = [int(input()) for _ in range(3)]
print(a ** b, pow(a, b, m), sep="\n")
