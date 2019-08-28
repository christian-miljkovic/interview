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

def romanToInt(s):
    
    if len(s) == 0:
        return 0
    
    lookup_table = {
        'IV':4,
        'X': 10,
        'XL':40,
        'XC':90,
        'CD':400,
        'CM':900
    }
    
    if s in lookup_table:
        return lookup_table[s]
    
    total = 0
    prev_val = None

    for i in range(0,len(s)):
        if s[i] == 'I':
            total += 1
            prev_val = 'I'
        elif s[i] == 'V':
            if prev_val == 'I':
                total -=1
                total += 4
                prev_val = None
            else:
                total += 5
        elif s[i] == 'X':
            if prev_val == 'I':
                total -= 1
                total += 9
                prev_val = None
            else:
                total += 10
                prev_val = 'X'
        elif s[i] == 'L':
            if prev_val == 'X':
                total -= 10
                total += 40
                prev_val = None
            else:
                total += 50
        elif s[i] == 'C':
            if prev_val == 'X':
                total -= 10
                total += 90
                prev_val = None
            else:
                total += 100
                prev_val = 'C'
        elif s[i] == 'D':
            if prev_val == 'C':
                total -= 100
                total += 400
                prev_val = None
            else:
                total += 500
        elif s[i] == 'M':
            if prev_val == 'C':
                total -= 100
                total += 900
                prev_val = None
            else:
                total += 1000
    
    return total

test_one = "III"
test_two = "IV"
test_three = "IX"
test_four = "LVIII"
test_five = "MCMXCIV"

print(romanToInt(test_one))
print(romanToInt(test_two))
print(romanToInt(test_three))
print(romanToInt(test_four))
print(romanToInt(test_five))
