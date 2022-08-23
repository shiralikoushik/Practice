"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

A subarray is a contiguous part of an array.

 

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Example 2:

Input: nums = [1]
Output: 1
Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23
"""


nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

max_sum = nums[0]
curr_sum = 0
for i in range(len(nums)):
    curr_sum += nums[i]
    if curr_sum < 0:
        max_sum = max(max_sum, curr_sum)
        curr_sum = 0
    else:
        max_sum = max(max_sum, curr_sum)

print(max_sum)
