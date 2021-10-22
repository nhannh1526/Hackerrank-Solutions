# Enter your code here. Read input from STDIN. Print output to STDOUT

import string

print(*sorted(input(), key=(string.ascii_letters + '1357902468').index), sep='')
