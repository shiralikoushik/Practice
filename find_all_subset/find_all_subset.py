"""
Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

 

Example 1:

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
Example 2:

Input: nums = [0]
Output: [[],[0]]

"""


nums = []
li1 = [[i] for i in nums]
if len(nums) != 1:
    li1.append(nums[:])
if nums != []:
    li1.append([])

# print(li1)
for i in nums:
    for j in nums:
        if (i != j) and ([i, j] not in li1) and ([j, i] not in li1):
            li1.append([i, j])

print(li1)
