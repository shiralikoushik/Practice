""" Largest number in a string """

import re
str1 = "100klh564abc365bg65"

res = re.findall(r'[0-9]+',str1)
x = map(int,res)
print(max(x))