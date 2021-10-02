#!/bin/python3

if __name__ == '__main__':
    s = input()
    d = {}
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1

    data = [[d[c], c] for c in d.keys()]
    data.sort(key=lambda x: [-x[0], x[1]])

    print(*[f"{item[1]} {item[0]}" for item in data[:3]], sep="\n")
