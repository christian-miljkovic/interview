"""
Given a non-empty array of integers, every element appears three times except for one, which appears exactly once. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,3,2]
Output: 3
Example 2:

Input: [0,1,0,1,0,1,99]
Output: 99

"""
# Time Complexity: O(nlogn)
# Space Complexity: O(1)

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        sorted_nums = sorted(nums)
        curr_num = sorted_nums[0]
        total = 0
        
        for i in range(0,len(sorted_nums),):
            if curr_num != sorted_nums[i]:
                if total < 3:
                    return curr_num
                else:
                    curr_num = sorted_nums[i]
                    total = 0
            
            total += 1
        
        if total < 3:
            return curr_num
        