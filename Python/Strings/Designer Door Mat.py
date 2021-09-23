# Enter your code here. Read input from STDIN. Print output to STDOUT

N, M = map(int, input().split())

center_row = N // 2
for row in range(N):
    if row < center_row:
        print((".|."*(row*2+1)).center(N*3, "-"))
    elif row == center_row:
        print("WELCOME".center(N*3, "-"))
    else:
        print((".|."*((N-row-1)*2+1)).center(N*3, "-"))
