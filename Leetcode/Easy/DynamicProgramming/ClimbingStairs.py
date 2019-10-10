"""
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.

Example 1:

Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
"""
# Tabulation
# Time Complexity: O(n)
# Time Complexity: O(1)
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        
        prev = 0
        curr = 1
        
        for i in range(n):
            tmp = prev + curr
            prev = curr
            curr = tmp
        
        return curr


# Memoization
class Solution:
    
    def climbRec(self, n: int, look_up: list) -> int:
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        elif n == 2:
            return 2
        elif n in look_up:
            return look_up[n]
        else:
            look_up[n] = self.climbRec(n-1,look_up) + self.climbRec(n-2,look_up)
        
        return look_up[n]
    
    def climbStairs(self, n: int) -> int:
        look_up = dict()
        return self.climbRec(n, look_up)