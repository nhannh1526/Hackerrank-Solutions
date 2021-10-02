def merge_the_tools(string, k):
    # your code goes here
    for i in range(0, len(string), k):
        distinct_characters = ""
        for char in string[i:i + k]:
            if char not in distinct_characters:
                distinct_characters += char
        print(distinct_characters)


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
