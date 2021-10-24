def cube(x): return x ** 3  # complete the lambda function


def fibonacci(n):
    # return a list of fibonacci numbers
    fibonacci_numbers = [0, 1]
    for i in range(2, n):
        fibonacci_numbers.append(fibonacci_numbers[i - 1] + fibonacci_numbers[i - 2])
    return fibonacci_numbers[0:n]


if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
