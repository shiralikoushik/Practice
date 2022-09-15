"""
Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].

Input: digits = [1,2,9]
Output: [1,3,0]
"""

digits = [4, 3, 2, 9]
x = list(map(str, digits))
y = "".join((x))
s = int(y) + 1
j = [i for i in str(s)]
print(j)
