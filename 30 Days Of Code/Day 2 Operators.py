#!/bin/python3


#
# Complete the 'solve' function below.
#
# The function accepts following parameters:
#  1. DOUBLE meal_cost
#  2. INTEGER tip_percent
#  3. INTEGER tax_percent
#


def solve(meal_cost, tip_percent, tax_percent):
    # Write your code here
    print(round(meal_cost * (1 + (tip_percent + tax_percent) * 0.01)))


if __name__ == '__main__':
    meal_cost = float(input().strip())

    tip_percent = int(input().strip())

    tax_percent = int(input().strip())

    solve(meal_cost, tip_percent, tax_percent)
