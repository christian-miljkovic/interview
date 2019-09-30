"""
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]

"""

# Initial Attempt Time Limit Exceeded -> Base case working
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        hash_map = dict()
        return_list = []
        is_visited = set()
        
        for num in nums:
            if num not in hash_map:
                hash_map[num] = 1
            else:
                hash_map[num] += 1
        
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                
                look_up_val = (nums[i] + nums[j])*-1
                key = tuple(sorted((nums[i],nums[j],look_up_val)))
                
                if (look_up_val in hash_map) and is_array_allowed(hash_map, key) and (key not in is_visited):
                    return_list.append([nums[i],nums[j],look_up_val])
                    is_visited.add(key)
        
        return return_list
            
def is_array_allowed(hash_map, arr):
    
    count_one = arr.count(arr[0])
    count_two = arr.count(arr[1])
    count_three = arr.count(arr[2])
        
    if hash_map[arr[0]] < count_one or hash_map[arr[1]] < count_two or hash_map[arr[2]] < count_three:
        return False
    
    return True