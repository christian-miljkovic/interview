"""
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"

"""

# Time Complexity: O(n^2)
# Space Complexity: O(1)

class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        if len(s) <= 1:
            return s
        
        longest_palindrome = ""
        
        for i in range(len(s)):
            
            temp_str = check_palindrome(s, i, i)
    
            if len(temp_str) > len(longest_palindrome):
                longest_palindrome = temp_str
            
            temp_str = check_palindrome(s, i, i+1)
            
            if len(temp_str) > len(longest_palindrome):
                longest_palindrome = temp_str
            
        return longest_palindrome
        
def check_palindrome(input_str, left, right):
    
    while left >= 0 and right < len(input_str) and input_str[left] == input_str[right]:
        left -= 1
        right += 1
    
    return input_str[left+1:right]