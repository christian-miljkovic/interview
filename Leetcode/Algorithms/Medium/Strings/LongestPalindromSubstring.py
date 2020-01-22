

# Time Complexity: O(n^2)
# Space Complexity: O(1)

class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        max_window = 0
        max_pos = (0,0)
        
        for i in range(0, len(s)):
            size_odd, pos = is_palindrome(i, i, s)
            if size_odd > max_window:
                max_pos = pos
                max_window = size_odd
            
            size_even, pos = is_palindrome(i, i + 1, s)
            if size_even > max_window:
                max_pos = pos
                max_window = size_even
        
        return s[max_pos[0]:max_pos[1]+1]
    
def is_palindrome(i, j, string):
    
    while i >= 0 and j < len(string) and string[i] == string[j]:        
        i -= 1
        j += 1
        
    i += 1
    j -= 1
    
    return (j - i + 1, (i, j))
        