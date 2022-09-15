"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.


"""


strs = ["flower","flow","flight"]
x = ""
y = []
for idx, i in enumerate(zip(*strs)):
    if len(set(i)) == 1:
        x += strs[0][idx]
        y.append(x)
    else:
        x = ""
if y:
    print(max(y))
else:
    print("")
