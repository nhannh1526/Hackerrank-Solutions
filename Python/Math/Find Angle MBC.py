# Enter your code here. Read input from STDIN. Print output to STDOUT

import math

AB, BC = int(input()), int(input())
print(round(math.degrees(math.atan2(AB, BC))), chr(176), sep='')
