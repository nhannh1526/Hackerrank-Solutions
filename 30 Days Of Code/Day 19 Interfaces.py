class AdvancedArithmetic(object):
    def divisorSum(n):
        raise NotImplementedError


class Calculator(AdvancedArithmetic):
    def divisorSum(self, n):
        divisors = []
        i = 1
        while i <= n**0.5:
            if n % i == 0:
                if n / i == i:
                    divisors.append(i)
                else:
                    divisors.extend([i, int(n / i)])
            i += 1
        return sum(divisors)


n = int(input())
my_calculator = Calculator()
s = my_calculator.divisorSum(n)
print("I implemented: " + type(my_calculator).__bases__[0].__name__)
print(s)
