# Enter your code here. Read input from sTDIN. Print output to sTDOUT

from collections import namedtuple

N = int(input())
columns = map(str, input().split())
student = namedtuple('student', columns)
marks = []

for i in range(N):
    marks.append(int(student(*input().split()).MARKS))

print(f"{sum(marks)/len(marks):.2f}")
