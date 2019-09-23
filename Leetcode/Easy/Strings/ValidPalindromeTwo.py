"""
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true
Example 2:

Input: "race a car"
Output: false
"""

# Time Comlpexity: O(n)
# Space Complexity: O(n)

class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) == 0:
            return True
        
        low_str = s.lower()
        alnum_list = []
        
        for char in low_str:
            if char.isalnum():
                alnum_list.append(char)
        
        rev_alnum_list = alnum_list[::-1]
        
        for i in range(0,len(alnum_list)):
            if alnum_list[i] != rev_alnum_list[i]:
                return False
                
        
        return True
        

