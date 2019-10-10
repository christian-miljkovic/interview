"""
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, two is written as II in Roman numeral, just two one's added together. Twelve is written as, XII, which is simply X + II. The number twenty seven is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer. Input is guaranteed to be within the range from 1 to 3999.

Example 1:

Input: "III"
Output: 3
Example 2:

Input: "IV"
Output: 4
Example 3:

Input: "IX"
Output: 9
Example 4:

Input: "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.
Example 5:

Input: "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
"""

"""
Input: str representing roman numeral 

Edge Cases:
- empty str
- subtraction ones

Solution: Read in reverse order and apply the speacial cases while adding to total

Output: convert str to integer between 1 and 3999

Notes:
larg -> small

"""
# Time Complexity: O(n) where n is the len of the string
# Space Complexity: O(1)
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0
        
        total = 0
        prev_char = None
        
        
        for i in range(len(s)-1,-1,-1):
            curr_char = s[i]
            
            if curr_char == 'I':
                if prev_char =='V' or prev_char == 'X':
                    total -= 1
                else:
                    total += 1
            
            elif curr_char == 'X':
                if prev_char == 'L' or prev_char == 'C':
                    total -= 10
                else:
                    total += 10
                    
            elif curr_char == 'C':
                if prev_char == 'D' or prev_char == 'M':
                    total -= 100
                else:
                    total += 100
            
            elif curr_char == 'V':
                total += 5
                
            elif curr_char == 'L':
                total += 50
                
            elif curr_char == 'D':
                total += 500
                
            elif curr_char == 'M':
                total += 1000
            
            else:
                total += 0
            
            prev_char = curr_char
                
            
        return total