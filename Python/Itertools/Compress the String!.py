# Enter your code here. Read input from STDIN. Print output to STDOUT

from itertools import groupby

print(*[tuple([len(list(g)), int(k)])
      for k, g in groupby(str(input()))], sep=" ")
