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

# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution1:
    def isPalindrome(self, s: str) -> bool:
        
        if not s:
            return True
        
        left, right = 0, len(s) - 1
        
        while left <= right:
            
            left_char = s[left].lower()
            right_char = s[right].lower()
            
            if left_char.isalnum() and right_char.isalnum() and left_char != right_char:
                return False
            
            if not left_char.isalnum() and right_char.isalnum():
                right += 1
            if not right_char.isalnum() and left_char.isalnum():
                left -= 1
                
            
            left += 1
            right -= 1
        
        return True
                


# Time Comlpexity: O(n)
# Space Complexity: O(n)

class Solution2:
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
        

