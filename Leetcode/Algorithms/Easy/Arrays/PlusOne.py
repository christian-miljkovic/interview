

# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        total = 0
        base = 1
        
        for num in reversed(digits):
            total += num * base
            base *= 10
        
        total += 1
        return [int(val) for val in str(total)]