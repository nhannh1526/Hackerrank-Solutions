# Enter your code here. Read input from STDIN. Print output to STDOUT

K = int(input())
room_number_list = list(map(int, input().split()))
print(((sum(set(room_number_list)) * K) - (sum(room_number_list))) // (K - 1))
