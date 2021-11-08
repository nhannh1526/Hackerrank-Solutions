# Enter your code here. Read input from STDIN. Print output to STDOUT

import re

for _ in range(int(input())):
    n = input().strip()
    try:
        assert re.match(r'(\d{4}-){3}\d{4}$', n) or re.match(r'\d{16}$', n)
        n = re.sub(r'-', '', n)
        assert re.match(r'[456]', n)
        assert not re.search(r'(\d)\1{3,}', n)
    except:
        print('Invalid')
    else:
        print('Valid')
