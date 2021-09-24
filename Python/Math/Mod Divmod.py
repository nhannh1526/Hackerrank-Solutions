# Enter your code here. Read input from STDIN. Print output to STDOUT

a, b = int(input()), int(input())
print("{0}\n{1}\n({0}, {1})".format(*divmod(a, b)))
