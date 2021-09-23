def print_rangoli(size):
    # your code goes here
    alphabet = list(map(chr, range(ord("a"), ord("z")+1)))

    lower = []
    for i in range(size):
        s = "-".join(alphabet[i:size])
        lower.append((s[::-1]+s[1:]).center(4*size-3, "-"))
    print('\n'.join(lower[::-1]+lower[1:]))


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
