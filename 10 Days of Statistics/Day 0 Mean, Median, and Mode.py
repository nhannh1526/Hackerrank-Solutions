# Enter your code here. Read input from STDIN. Print output to STDOUT

import statistics

from scipy import stats

N = int(input())
arr = list(map(int, input().split()))

print(round(statistics.mean(arr), 1),
      round(statistics.median(arr), 1),
      stats.mode(arr)[0][0], sep="\n")
