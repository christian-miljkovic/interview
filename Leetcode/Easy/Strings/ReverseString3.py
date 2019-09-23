"""
Given a string, you need to reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

Example 1:
Input: "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"
Note: In the string, each word is separated by single space and there will not be any extra space in the string.
"""

# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def reverseWords(self, s: str) -> str:
        
        str_list = s.split(" ")
        for index, word in enumerate(str_list):            
            str_list[index] = word[::-1]
        
        return ' '.join(str_list)