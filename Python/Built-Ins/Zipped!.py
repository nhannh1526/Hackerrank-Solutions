# Enter your code here. Read input from STDIN. Print output to STDOUT

[print(sum(marks) / len(marks)) for marks in zip(*[map(float, input().split())
                                                   for _ in range(list(map(int, input().split()))[1])])]
