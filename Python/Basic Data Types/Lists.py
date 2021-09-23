if __name__ == '__main__':
    N = int(input())
    _list = []
    for _ in range(N):
        command = input().split()
        args = command[1:]
        command = command[0]
        if command == "print":
            print(_list)
        else:
            command += "(" + ",".join(args) + ")"
            eval("_list."+command)
