"""
There is a fence with n posts, each post can be painted with one of the k colors.

You have to paint all the posts such that no more than two adjacent fence posts have the same color.

Return the total number of ways you can paint the fence.

Note:
n and k are non-negative integers.

Example:

Input: n = 3, k = 2
Output: 6
Explanation: Take c1 as color 1, c2 as color 2. All possible ways are:

            post1  post2  post3      
 -----      -----  -----  -----       
   1         c1     c1     c2 
   2         c1     c2     c1 
   3         c1     c2     c2 
   4         c2     c1     c1  
   5         c2     c1     c2
   6         c2     c2     c1
"""

class Solution(object):
    def numWays(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        if n == 0:
            return 0
        elif n == 1:
            return k
        elif n == 2:
            return k*1 + k*(k-1)
        
        else:
            # diff represents a set of fences that are all being painted differently
            # same represents the fences that are being constantly painted the same 
            same = k*1
            diff = k*(k-1)
            
            for i in range(3,n+1):
                # There are two options here either keep painting different thus (k-1) or because its the same fence we have to anyway change it thus (k-1)
                old_diff = diff
                diff = diff*(k-1) + same*(k-1)
                same = old_diff
        
            return same + diff
