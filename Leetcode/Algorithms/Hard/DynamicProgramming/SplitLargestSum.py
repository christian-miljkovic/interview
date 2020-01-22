class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        
        memo = collections.defaultdict(dict)
        return split_naive(nums, 0, m, memo)
        
        
        
def split_naive(nums, split_index, m, memo):
    
    if split_index == len(nums):
        return 0
    elif m == 1:
        return sum(nums[split_index:])
    elif split_index in memo and m in memo[split_index]:
        return memo[split_index][m]
    
    else:
        memo[split_index][m] = float('inf')

        for i in range(1, len(nums) + 1):
            left = sum(nums[split_index:split_index+i])
            right = split_naive(nums, split_index+i, m - 1, memo)
            memo[split_index][m] = min(memo[split_index][m], max(left, right))    
            if left > right:
                break
        
        return memo[split_index][m]