"""
Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Example:

Input:  [1,2,3,4]
Output: [24,12,8,6]
Note: Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity analysis.)
"""

# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        answer = [1]*len(nums)
        L = 1
        
        for i in range(1,len(nums)):
            L *= nums[i-1]
            answer[i] = L
        
        R = 1
        
        for j in range(len(nums)-2,-1,-1):            
            R *= nums[j+1]
            answer[j] *= R
        
        return answer