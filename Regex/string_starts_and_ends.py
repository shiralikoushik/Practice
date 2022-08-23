""" Check whether a string starts and ends with the same character or not (using Regular Expression)"""

import re

str1 = "abba"

pattern = r"^[a-zA-Z]$|^([a-zA-Z]).*\1$"

a = re.search(pattern, str1)
print(a.group(0))
if a:
    print("valid")
else:
    print("Invalid")

# print(a)
