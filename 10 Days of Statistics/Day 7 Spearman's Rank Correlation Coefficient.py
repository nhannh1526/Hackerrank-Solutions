# Enter your code here. Read input from STDIN. Print output to STDOUT

def get_rank(a):
    return [sorted(a).index(i) for i in a]


def spearmanr(a, b):
    n = len(a)
    rank_a = get_rank(a)
    rank_b = get_rank(b)
    d = sum([(ra - rb) ** 2 for ra, rb in zip(rank_a, rank_b)])
    return 1 - ((6 * d) / (n ** 3 - n))


n = int(input())
X = list(map(float, input().split()))
Y = list(map(float, input().split()))

print(f"{spearmanr(X, Y):.3f}")
