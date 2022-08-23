import re

text_reg = """
Mr. Sony
Mr Samsung
Ms Google
Mrs. Apple
Mr. Amazon

KoushikShirali@gmail.com
kousik.shirali@rvce.edu
koushik-123-shirali@my-work.net

https://www.google.com
http://coreyms.com
https://youtube.com
https://isro.gov.in

111-222-333
444.555.666
696*696*696
"""
str1 = " Is This is the example string"
def ret_num(pattern,str1):
    pattern1 = re.compile(pattern)
    return pattern1.findall(str1)
# pattern = re.compile(r"[a-z]")

# m = pattern.findall(str1)
lower_case = len(ret_num(r'[a-z]',str1))
upper_case = len(ret_num(r'[A-Z]',str1))
numeric = len(ret_num(r'[0-9]',str1))
#speci_char = len(ret_num(r'[+-?_:]',str1))
print(lower_case,upper_case,numeric)
#pattern1 = re.compile(r'This')

#res = re.search(r'[a-z]',str1)
# if res != None:
#     print(True)
# else:
#     print(False)
#print(m)
# for match in matches:
#     print(match)