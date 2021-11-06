# Enter your code here. Read input from STDIN. Print output to STDOUT

import re

regex_pattern = r"[\s:](#[a-f0-9]{6}|#[a-f0-9]{3})"

for _ in range(int(input())):
    css_code = input()
    [print(hex_color_code)
     for hex_color_code in re.findall(regex_pattern, css_code, re.I)]
