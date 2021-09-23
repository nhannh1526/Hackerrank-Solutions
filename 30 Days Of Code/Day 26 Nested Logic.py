# Enter your code here. Read input from STDIN. Print output to STDOUT

class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year


date_returned = Date(*map(int, input().split()))
date_due = Date(*map(int, input().split()))

if date_returned.year == date_due.year:
    if date_returned.month > date_due.month:
        fine = 500 * (date_returned.month - date_due.month)
    elif date_returned.month == date_due.month:
        if date_returned.day > date_due.day:
            fine = 15 * (date_returned.day - date_due.day)
        else:
            fine = 0
    else:
        fine = 0
elif date_returned.year > date_due.year:
    fine = 10000
else:
    fine = 0

print(fine)
