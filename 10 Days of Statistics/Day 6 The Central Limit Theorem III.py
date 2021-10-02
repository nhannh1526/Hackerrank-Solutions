# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())
mu, sigma = int(input()), int(input())
interval, z = float(input()), float(input())

sigma = sigma / n ** 0.5
print(f"{mu - sigma * z:.2f}",
      f"{mu + sigma * z:.2f}", sep="\n")
