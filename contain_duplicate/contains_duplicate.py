""" Return true if a list contains duplicate else return false"""

nums = [1, 2, 4, 3, 3, 5]
num2 = list(set(nums))
if len(num2) == len(nums):
    print(False)
else:
    print(True)
