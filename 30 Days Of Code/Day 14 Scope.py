class Difference:
    def __init__(self, a):
        self.__elements = a

    # Add your code here
    def computeDifference(self):
        if len(self.__elements) == 1:
            self.maximumDifference = self.__elements[0]
        elif len(self.__elements) == 2:
            self.maximumDifference = abs(
                self.__elements[0] - self.__elements[1])
        else:
            self.maximumDifference = abs(
                self.__elements[0] - self.__elements[1])
            for i in range(len(self.__elements)-1):
                for j in range(1, len(self.__elements)):
                    current_difference = abs(
                        self.__elements[i] - self.__elements[j])
                    if current_difference > self.maximumDifference:
                        self.maximumDifference = current_difference

# End of Difference class


_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)
