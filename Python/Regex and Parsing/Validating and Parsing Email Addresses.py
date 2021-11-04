# Enter your code here. Read input from STDIN. Print output to STDOUT

import email.utils
import re

for _ in range(int(input())):
    name, email_address = map(str, email.utils.parseaddr(input()))

    validEmail = re.search(
        r'^[a-zA-Z]+[a-zA-Z0-9_.-]+[@][a-zA-Z]+[.][a-zA-Z]{1,3}$', email_address)
    if validEmail:
        print(email.utils.formataddr((name, email_address)))
