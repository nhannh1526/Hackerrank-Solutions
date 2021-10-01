# Enter your code here. Read input from STDIN. Print output to STDOUT

muA, muB = map(float, input().split())
print(f"{160 + 40 * (muA + muA**2):.3f}",
      f"{128 + 40 * (muB + muB**2):.3f}", sep="\n")
