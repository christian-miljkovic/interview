"""
Longest Substring Without Repeating Characters

Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""


# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        if not s:
            return 0
        
        char_mapping = collections.defaultdict(list)
        max_size = 0        
        start = 0
        
        for end, char in enumerate(s):        
            
            if char in char_mapping:
                start = max(char_mapping[char] + 1, start)
                char_mapping[char] = end
            else:
                char_mapping[char] = end
                
            max_size = max(max_size, end - start + 1)
                
        return max(max_size, end - start + 1)