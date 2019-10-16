"""
Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

Example 1:

Input: 121
Output: true
Example 2:

Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
"""

class Solution:
    # Fastest solution by conerting to string
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        if str(x) == str(x)[::-1]:
            return True
        
        return False
            

class Solution:
    # Slower solution by making calculations
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        elif x == 0:
            return True
        
        x_copy = x
        count_bases = -1
        
        while x > 0:
            x = x//10
            count_bases += 1
           
        reversed_x = 0
        x_copy_two = x_copy
        base = 10
        
        while x_copy:
            
            tmp = x_copy%10
            if count_bases == 0:
                reversed_x += tmp
            else:
                reversed_x += tmp * (base ** count_bases)
            
            x_copy = x_copy//10
            count_bases -= 1
        
        return x_copy_two == reversed_x
        
            