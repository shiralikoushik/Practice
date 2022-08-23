"""
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

 

Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.

"""
nums = [[1,3],[2,6],[8,10],[15,18],[16,19],[27,30]]
nums.sort()
cur = nums[0][:]
x = []
for i in nums:
    
    if cur[0] <= i[0]:
        if cur[1] >= i[0] and cur[1] <= i[1]:
            cur[0] = min(cur[0],i[0])
            cur[1] = max(cur[1],i[1])
            if i == nums[-1]:
                x.append(cur)
        else:
            if i == nums[-1]:
                x.append(cur)
                if i[0] not in range(cur[0],cur[1]+1) and i[1] not in range(cur[0],cur[1]+1):
                    x.append(i)
            else:
            
                x.append(cur)
                cur = i[:]
        

print(x)  