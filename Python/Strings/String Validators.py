if __name__ == '__main__':
    s = input()
    for cmd in [".isalnum()", ".isalpha()", ".isdigit()", ".islower()", ".isupper()"]:
        print(any([eval("c"+cmd) for c in s]))
