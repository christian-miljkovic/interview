"""
A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

Write a function to determine if a number is strobogrammatic. The number is represented as a string.

Example 1:

Input:  "69"
Output: true
Example 2:

Input:  "88"
Output: true
Example 3:

Input:  "962"
Output: false

"""

"""
1 6 8 9 0
10 -> no
11 -> yes
69 -> yes

"""
# Time Complexity: O(n) where n is the length of the string
# Space Complexity: O(n)


class Solution(object):
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        non_strobo_set = {"2","3","4","5","7"}                
        rev_num = num[::-1]
        
        for i in range(0,len(num)):
            if num[i] in non_strobo_set:
                return False
            if num[i] == '6' and rev_num[i] != '9':
                return False
            elif num[i] == '9' and rev_num[i] != '6':
                return False
            
            elif num[i] != '9' and num[i] != '6':
                if num[i] != rev_num[i]:
                    return False
        
        
        return True
                
        
        
        
        
        