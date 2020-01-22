"""
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

Example 1:

Input: [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.
Example 2:

Input: [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
             Total amount you can rob = 2 + 9 + 1 = 12.

"""

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return rob_house_recursively(nums, i=len(nums)-1, look_up=dict())

# Recursive with top-down memoization         
def rob_house_recursively(nums, i, look_up):
    
    if i < 0:
        return 0
    
    if i in look_up:
        return look_up[i]
    
    else:
        look_up[i] = max(rob_house_recursively(nums, i-1, look_up), rob_house_recursively(nums, i-2, look_up) + nums[i])
        return look_up[i]

# 
def rob_house_iteratively(nums, look_up):
    
    if len(nums) == 0:
        return 0
    
    look_up[0] = 0
    look_up[1] = nums[0]
    
    for i in range(1,len(nums)):
        val = nums[i]
        look_up[i+1] = max(look_up[i],look_up[i-1] + val)
    
    return look_up[len(nums)]