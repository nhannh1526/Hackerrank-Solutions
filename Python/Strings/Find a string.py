def count_substring(string, sub_string):
    return len([i for i in range(len(string) - len(sub_string) + 1) if string[i:].startswith(sub_string)])


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)
