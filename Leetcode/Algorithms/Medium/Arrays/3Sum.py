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

# Time Compelxity: O(n*n)
# Space Complexity: O(n)

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        # sort list
        return_map = collections.defaultdict(list)
        nums = sorted(nums)

        # [-1, 0, 1, 2, -1, -4] -> [-4, -1, -1, 0, 1, 2]
        for index in range(len(nums)):
            solution = binary_search(nums, index, index+1, len(nums) - 1)
            if solution:
                for temp_list in solution:
                    return_map[str(temp_list)] = temp_list
    
        return [val for key, val in return_map.items()]
        
def binary_search(nums, start_index, left_index, right_index):
    
    return_list = []
    
    while left_index < right_index:
        
        new_sum = nums[start_index] + nums[left_index] + nums[right_index]
        
        if new_sum > 0:
            right_index -= 1
        elif new_sum < 0:
            left_index += 1
        else:
            return_list.append(sorted([nums[start_index], nums[left_index], nums[right_index]]))
            while left_index < right_index and nums[left_index] == nums[left_index+1]:
                left_index += 1
            while left_index < right_index and nums[right_index] == nums[right_index-1]:
                right_index -= 1
            
            left_index += 1
            right_index -= 1
            
        
    return return_list



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



