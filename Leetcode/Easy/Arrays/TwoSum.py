'''
Description: 

Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.
'''

# Brute Force Approach
# Time Complexity: O(n^2)
# Space Complexity O(1)
def twoSum(self, nums, target):
    for i in range(0,len(nums)):
        for j in range(1,len(nums)):
            if nums[i] + nums[j] == target and i != j :
                return [i,j]

# Two Pass Hash Table
# Time Complexity: O(n)
# Space Complexity: O(n)
def twoSumHashTwo(self, nums, target):
    hashTable = dict()
    for i in range(0,len(nums)):
        hashTable[nums[i]] = i
    
    for j in range(0, len(nums)):
        difference = target - nums[j]
        if(difference in hashTable):
            if(hashTable[difference] != j):
                return [j, hashTable[difference]]


# Reviewed version 
# Space Complexity: O(n)
# Time Complexity: O(n)

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hash_map = collections.defaultdict(list)
        
        for index, num in enumerate(nums):
            hash_map[num].append(index)
            
        for index, num in enumerate(nums):
            k = target - num
            
            if k in hash_map:
                for i in hash_map[k]:
                    for j in hash_map[num]:
                        if i != j:                            
                            return [i, j]